# Practical Exercise - Unit Tests & Model/View Philosophy - Python

This exercise relies on the BiBook project, the upcoming next-generation platform to borrow books. It shows an application whose logics is not testable yet.

## Virtual environment

Install `pipenv`:

```
pip install pipenv
```

> Note: On Linux it may be `pip3` instead of `pip`.

Install dependencies:

```
pipenv install --dev
```

> Note: On Linux `pipenv` may not be available, so run `python -m pipenv install --dev`.

Now you can run the following commands:

Run application:

```
pipenv run python -m bibook
```

Run linter:

```
pipenv run pylint bibook
```

Run unit tests:

```
pipenv run pytest
```
