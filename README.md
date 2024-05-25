# :page_facing_up: HTML Converter Kata :page_facing_up:

[![Python](https://img.shields.io/badge/Python-3.12+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)

## Resources

These instructions where extracted from Emily Bache repository. The link to the original repository can be found in the link bellow.

[![Web](https://img.shields.io/badge/GitHub-emilybache-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/emilybache/Racing-Car-Katas)

## Description

This kata is part of the Racing Kart Kata series, which is a set of exercises to practice TDD and SOLID principles.

There are several variants of this exercise in this repo. They all present slightly different challenges. You can expect to learn more about 
test design, SOLID principles and testability by working on them.

As a first step, try to get some kind of test in place before you change the class at all. If the tests are hard to write, is that because 
of the problems with SOLID principles?

When you have some kind of test to lean on, refactor the code and make it testable. Take care when refactoring not to alter the functionality, 
or change interfaces which other client code may rely on. Add more tests to cover the functionality of the particular class you've been asked to get under test.

### UnicodeFileToHtmlTextConverter

Write the unit tests for the UnicodeFileToHtmlTextConverter class. This class is designed to reformat a plain text file for display in a browser.

Bonus: identify which of the SOLID principles this code violates.

### HtmlPagesConverter

Write the unit tests for the HtmlPagesConverter class. This class is designed to reformat a plain text file for display in a browser, one page at a time.

### HtmlConverter

Write unit tests that expose the bugs. Bugs are marked with a comment in the code. You should preserve the original interface to the class.

## Objective

The objective of the kata is to identify the SOLID principle that is not being followed and refactor the code to make it testable and maintainable.

We will learn how to work with legacy code that is difficult to test and learn how to refactor step by step. We can use Mocks, Stubs or none at all to test the code.

## Configuration

The project can be configured with `poetry` and `pyenv`.
1. Install python version with pyenv:
    ```bash
    pyenv install 3.12.0
    ```
2. Install poetry:
    ```bash
    pip install poetry
    ```
3. Create a virtual environment and install dependencies:
    ```bash
    poetry install
    poetry install --dev
    ```
   
    By default, it will create the virtual environment outside the project. To create it inside, use the following command:
    ```bash
    poetry config virtualenvs.in-project true
    poetry install
    ```
4. Activate the virtual environment:
   ```bash
    poetry shell
    ```
   You can activate it manually running `source .venv/bin/activate` on Unix systems or `source .venv/Scripts/activate` on Windows.

## Running the tests

To run the tests, execute one of the following commands:

```bash
pytest
```

or

```bash
poetry run pytest
```

### Visit my GitHub profile to see all solved katas 🚀

[![Web](https://img.shields.io/badge/GitHub-Dimanu.py-14a1f0?style=for-the-badge&logo=github&logoColor=white&labelColor=101010)](https://github.com/dimanu-py/code-katas)


