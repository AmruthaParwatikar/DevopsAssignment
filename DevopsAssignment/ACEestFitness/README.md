# ACEest_Fitness_Project

![CI](https://github.com/<your-username>/ACEest_Fitness_Project/actions/workflows/ci.yml/badge.svg)

A simple **Flask-based fitness membership management API** with Dockerized deployment and GitHub Actions CI/CD.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Setup & Local Run](#setup--local-run)
- [API Endpoints](#api-endpoints)
- [Running Tests](#running-tests)
- [Docker Build & Run](#docker-build--run)
- [CI/CD Pipeline](#cicd-pipeline)
- [Contributing](#contributing)
- [License](#license)

---

## Project Overview

`ACEest_Fitness_Project` is a RESTful API built with **Flask** to manage fitness members.  
It provides endpoints to **view members**, **add new members**, and is fully **containerized with Docker** for easy deployment.  
Unit tests are included and run automatically in **GitHub Actions CI/CD**, both locally and inside the Docker image.

---

## Features

- Flask REST API
- Sample member management endpoints
- Unit testing with **Pytest**
- Docker containerization
- GitHub Actions CI/CD
- Conventional commit-friendly branching

---

## Project Structure

```
ACEest_Fitness_Project/
│── ACEest_Fitness.py          # Main Flask app
│── requirements.txt           # Python dependencies
│── Dockerfile                 # Docker configuration
│── README.md                  # Project documentation
│── app/
│   ├── __init__.py            # Makes `app` a Python package
│   └── routes.py              # Flask route definitions
│── tests/
│   └── test_app.py            # Pytest tests
│── .github/workflows/ci.yml   # GitHub Actions workflow
```

---

## Requirements

- Python 3.10+
- pip
- Docker (optional, for containerization)
- Git & GitHub account

---

## Setup & Local Run

### 1. Clone & open project

```bash
# macOS/Linux
cd ~/Downloads
unzip ACEest_Fitness_Project.zip -d ~/Projects
cd ~/Projects/ACEest_Fitness_Project

# Windows PowerShell
cd $env:USERPROFILE\Downloads
Expand-Archive -Path .\ACEest_Fitness_Project.zip -DestinationPath $env:USERPROFILE\Projects
cd $env:USERPROFILE\Projects\ACEest_Fitness_Project

# Open in VS Code (optional)
code .
```

### 2. Create & activate virtual environment

```bash
# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows PowerShell
python -m venv .venv
. .\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Run Flask app

```bash
python ACEest_Fitness.py
```

Visit: [http://localhost:5000](http://localhost:5000)

**Quick Checks:**

- `/` → Welcome JSON  
- `/members` (GET) → Sample members list

---

## API Endpoints

| Endpoint         | Method | Description                     |
|-----------------|--------|---------------------------------|
| `/`             | GET    | Welcome message                 |
| `/members`      | GET    | List all members                |
| `/members`      | POST   | Add a new member                |

---

## Running Tests

```bash
pytest -v
```

Tests included:

- `test_home`
- `test_get_members`
- `test_add_member`

---

## Docker Build & Run

### 1. Build Docker image

```bash
docker build -t aceest_fitness:latest .
```

### 2. Run container

```bash
docker run --rm -p 5000:5000 aceest_fitness:latest
```

Test in browser: [http://localhost:5000](http://localhost:5000)

### 3. Run tests inside Docker

```bash
docker run --rm -w /app aceest_fitness:latest pytest -v
```

---

## CI/CD Pipeline

This project uses **GitHub Actions**:

- On push or pull request to `main`:
  - Builds Docker image
  - Runs Pytest **inside the container**
- Workflow file: `.github/workflows/ci.yml`
- Check results in the **Actions** tab

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-test-in-docker:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/setup-buildx-action@v3
      - run: docker build -t aceest_fitness:ci .
      - run: docker run --rm -w /app aceest_fitness:ci pytest -v
```
---

## Contributing

- Use **feature branches**:  
  ```bash
  git checkout -b feat/add-membership-upgrade
  git commit -m "feat(members): add membership upgrade endpoint"
  git push -u origin feat/add-membership-upgrade
  ```
- Open PR → CI/CD runs automatically
- Follow **conventional commits** (feat:, fix:, docs:, chore:)

---

## License

This project is open-source and free to use.
