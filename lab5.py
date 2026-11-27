from datetime import date
from enum import Enum


class MovieType(Enum):
    ACTION = "Action"
    COMEDY = "Comedy"
    DRAMA = "Drama"
    FANTASY = "Fantasy"


class Movie:
    def __init__(
        self,
        movie_id: int,
        title: str,
        ranking: float,
        release_date: str,
        character_number: int,
        ticket_price: int,
        comment: str,
        movie_type: MovieType,
        show_date: str,
        tickets_sold: int,
    ):
        if type(movie_id) is not int:
            raise TypeError("movie_id must be an integer")
        if movie_id <= 0:
            raise ValueError("movie_id must be positive")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title must be a non-empty string")
        if isinstance(ranking, bool) or not isinstance(ranking, (int, float)):
            raise TypeError("ranking must be a number")
        if not 0 <= ranking <= 10:
            raise ValueError("ranking must be between 0 and 10")
        for value, name in (
            (release_date, "release_date"),
            (show_date, "show_date"),
        ):
            if not isinstance(value, str):
                raise TypeError(f"{name} must be a string")
            try:
                date.fromisoformat(value)
            except ValueError as error:
                raise ValueError(f"{name} must be a valid ISO date") from error
        if type(character_number) is not int:
            raise TypeError("character_number must be an integer")
        if character_number < 0:
            raise ValueError("character_number cannot be negative")
        if isinstance(ticket_price, bool) or not isinstance(
            ticket_price, (int, float)
        ):
            raise TypeError("ticket_price must be a number")
        if ticket_price < 0:
            raise ValueError("ticket_price cannot be negative")
        if not isinstance(comment, str):
            raise TypeError("comment must be a string")
        if not isinstance(movie_type, MovieType):
            raise TypeError("movie_type must be a MovieType")
        if type(tickets_sold) is not int:
            raise TypeError("tickets_sold must be an integer")
        if tickets_sold < 0:
            raise ValueError("tickets_sold cannot be negative")

        self.id = movie_id
        self.title = title
        self.ranking = ranking
        self.release_date = release_date
        self.character_number = character_number
        self.ticket_price = ticket_price
        self.comment = comment
        self.movie_type = movie_type
        self.show_date = show_date
        self.tickets_sold = tickets_sold

    def get_ticket_price(self):
        return self.ticket_price

    def set_ticket_price(self, price):
        if price >= 0:
            self.ticket_price = price
        else:
            print("Ціна не може бути від'ємною")

    def show_info(self):
        print(f"{self.id}. {self.title} — {self.movie_type.value}")
        print(f"Рейтинг: {self.ranking}, " f"випуск: {self.release_date}")
        print(f"Персонажів: {self.character_number}")
        print(f"Ціна: {self.ticket_price} грн, " f"коментар: {self.comment}")
        print(f"Показ: {self.show_date}, " f"квитків: {self.tickets_sold}")
        print()

    def __del__(self):
        if hasattr(self, "title"):
            print(f"Видалено фільм: {self.title}")


class Cinema:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.movies = []

    def add_movie(self, movie):
        self.movies.append(movie)

    def get_movies(self):
        return self.movies.copy()

    def select_movies(self, min_ranking, max_price):
        for movie in self.movies:
            if (
                movie.ranking >= min_ranking
                and movie.ticket_price <= max_price
            ):
                movie.show_info()

    def sort_movies(self):
        self.movies.sort(key=get_release_date)

    def show_info(self):
        print(f"Кінотеатр: {self.name}, адреса: {self.location}")
        for movie in self.movies:
            movie.show_info()

    def __del__(self):
        print(f"Видалено кінотеатр: {self.name}")


def get_release_date(movie):
    return movie.release_date


def calculate_profit(movies, day):
    total = 0
    for movie in movies:
        if movie.show_date == day:
            total += movie.ticket_price * movie.tickets_sold
    return total


def main():
    movie1 = Movie(
        1,
        "Останній рейс",
        8.5,
        "2024-05-10",
        12,
        180,
        "Динамічний сюжет",
        MovieType.ACTION,
        "2026-11-18",
        50,
    )
    movie2 = Movie(
        2,
        "Веселі сусіди",
        7.8,
        "2022-09-15",
        8,
        150,
        "Легка комедія",
        MovieType.COMEDY,
        "2026-11-18",
        40,
    )
    movie3 = Movie(
        3,
        "Дорога додому",
        9.0,
        "2023-02-20",
        6,
        170,
        "Зворушлива історія",
        MovieType.DRAMA,
        "2026-11-19",
        30,
    )

    cinema = Cinema("Обрій", "Львів")
    cinema.add_movie(movie1)
    cinema.add_movie(movie2)
    cinema.add_movie(movie3)

    cinema2 = Cinema("Планета Кіно", "Львів")
    cinema2.add_movie(movie1)
    cinema2.add_movie(movie2)
    cinema2.add_movie(movie3)

    for movie in cinema2.movies:
        movie.show_info()

    movie1.set_ticket_price(190)
    print("Нова ціна:", movie1.get_ticket_price())

    print("\nФільми за датою випуску:")
    cinema.sort_movies()
    cinema.show_info()

    print("Фільми з рейтингом від 8 і ціною до 200 грн:")
    cinema.select_movies(8, 200)

    profit = calculate_profit(cinema.get_movies(), "2026-11-18")
    print(f"Виручка за 2026-11-18: {profit} грн")

    print(cinema.name)


if __name__ == "__main__":
    main()
