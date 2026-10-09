# Arena GitHub integration test

A disposable project containing synthetic drafting measurements. No drawings,
credentials, or production code are included. This checks whether Arena can read
a repository, implement a bounded task, run tests, and deliver a pull request.

## Task

Implement `to_millimeters(value, unit)` in `measurement.py`.

- Accept finite, nonnegative Python `int` and `float` values; reject booleans.
- Supported units are `mm`, `cm`, `m`, `in`, and `ft`, case-insensitively, with
  surrounding whitespace ignored.
- Conversion factors: 1, 10, 1000, 25.4, and 304.8 respectively.
- Return a float. Raise `ValueError` for unsupported units or invalid values,
  including negative numbers, infinity, NaN, strings, and null.
- Do not modify the tests, workflow, or project instructions.

Run `python -m unittest discover -s tests -v`. The starter intentionally fails
because the implementation is missing. Arena should make the checks pass and
open a pull request. Codex will review the patch before any merge.

These tests do not execute AutoCAD or validate drawings.
