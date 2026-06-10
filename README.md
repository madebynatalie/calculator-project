# Command-Line Calculator

## Overview

This project is a Python command-line calculator application that follows the REPL (Read-Eval-Print Loop) design pattern. Users can continuously perform arithmetic operations until they choose to exit the application.

## Features

* Addition
* Subtraction
* Multiplication
* Division
* Input validation
* Error handling for invalid inputs
* Division-by-zero protection
* Unit testing with pytest
* Parameterized testing
* 100% test coverage

## Project Structure

calculator_project/

* calculator/

  * operations.py
  * cli.py

* tests/

  * test_operations.py
  * test_cli.py

* README.md

* requirements.txt

* pytest.ini

## Setup

### Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python3 -m calculator.cli
```

## Running Tests

```bash
pytest
```

## Coverage

This project uses pytest-cov and achieves 100% test coverage.
