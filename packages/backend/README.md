# Backend

## Prerequisites

- Google Cloud SDK
    - `curl https://sdk.cloud.google.com | bash`
- Pipenv
    - `brew install pipenv`
- mypy
    - `brew install mypy`
- Yarn
    - `brew install yarn`

## Setup

```
pipenv install -d
pipenv run pip install -r <(pipenv lock -r) -t lib
yarn
```

## Test

```
pipenv run pytest --cov=app -n 2 tests
```

## Format and Lint with lint-staged

See [package.json](./package.json) and [setup.cfg](./setup.cfg).

Double quotes are warned with flake8-quotes.
