# Backend

## Prerequisites

- Google Cloud SDK
    - `curl https://sdk.cloud.google.com | bash`
- Pipenv
    - `brew install pipenv`
- mypy
    - `brew install mypy`
- FFFFFF
    - `python3 -m pip install --user ffffff`

## Setup

```
pipenv install -d
pipenv run pip install -r <(pipenv lock -r) -t lib
```

## Test

```
pipenv run pytest --cov=app -n 2 tests
```

## Format and Lint with lint-staged

1. Sort imports with isort
2. Format with FFFFFF
3. Lint with flake8
4. Lint with mypy

See [package.json](./package.json) and [setup.cfg](./setup.cfg) for details.
