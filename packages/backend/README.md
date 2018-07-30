# Backend

## Prerequisites

- Google Cloud SDK
    - `curl https://sdk.cloud.google.com | bash`
- Pipenv
    - `brew install pipenv`
- mypy
    - `brew install mypy`

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

See [package.json](./package.json) and [setup.cfg](./setup.cfg).

Double quotes are warned with flake8-quotes.
