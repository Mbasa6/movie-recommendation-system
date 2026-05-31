# Contributing to Movie Recommendation System

Thank you for your interest in contributing to this project.

## Prerequisites

Before contributing, ensure you have:

* Python 3.14+
* Git
* FastAPI
* Pytest

## Project Setup

Clone the repository:

```bash
git clone <repository-url>
```

Install dependencies:

```bash
pip install fastapi uvicorn pytest httpx
```

Run tests:

```bash
pytest
```

Run the API:

```bash
uvicorn api.main:app --reload
```

## Coding Standards

* Follow Python naming conventions.
* Write clear and maintainable code.
* Add tests for new functionality.
* Ensure all tests pass before submitting changes.

## How to Contribute

1. Fork the repository.
2. Create a feature branch.
3. Select an issue labeled `good-first-issue`.
4. Implement the solution.
5. Add or update tests.
6. Submit a Pull Request.

## Pull Request Requirements

* Clear description of changes.
* Related issue reference.
* Passing GitHub Actions workflow.
* No failing tests.
