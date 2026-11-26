---
name: jatsuk-review
description: Review and fix Python code for PEP 8, PEP 20, and Pylint compliance.
---

# Python Code Review

## Scope

Review the Python files specified by the user. If the scope is unclear, ask before
changing files.

## Workflow

1. Inspect the code, relevant tests, and existing Python and Pylint configuration.
2. Run Pylint on the scoped files using the project's environment and configuration.
   If Pylint is unavailable, report the blocker and ask before installing it.
3. Fix every reported Pylint issue without suppressing diagnostics, weakening
   configuration, or changing intended behavior.
4. Check and fix PEP 8 issues. Follow existing project configuration where it
   explicitly differs from PEP 8.
5. Apply PEP 20 principles to improve clarity and simplicity without unnecessary
   refactoring or speculative changes.
6. Run Pylint again and execute relevant tests. Repeat until Pylint reports no
   issues, or explain any issue that cannot safely be fixed.

## Constraints

- Preserve public interfaces and behavior unless the user approves a change.
- Do not modify unrelated files.
- Do not add lint suppressions or change lint rules merely to pass.
- Ask before making changes that require a significant design decision.

## Report

Summarize the changes, commands run, and results. Clearly identify any remaining
diagnostics, blocked checks, or unverified behavior.