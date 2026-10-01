# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Commands

```bash
# Install test dependency
pip install pytest

# Run all tests
pytest

# Run a single test
pytest test_hello.py::test_greet_with_name
```

## Architecture

Flat single-module Python project — no packages, no build system, no external dependencies beyond pytest.

- [hello.py](hello.py) — exports `greet(name: str) -> str`; strips whitespace, falls back to `"Hello, World!"` on empty input
- [test_hello.py](test_hello.py) — pytest suite covering normal names, empty strings, Unicode (Hebrew), and whitespace trimming

CI runs on every push/PR via [.github/workflows/tests.yml](.github/workflows/tests.yml) using Python 3.14.
