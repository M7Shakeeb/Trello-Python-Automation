# Trello API Automation Framework

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=for-the-badge&logo=docker&logoColor=white)
[![Dockerized Python Tests](https://github.com/M7Shakeeb/Trello-Python-Automation/actions/workflows/docker-tests.yml/badge.svg)](https://github.com/M7Shakeeb/Trello-Python-Automation/actions/workflows/docker-tests.yml)

## Project Overview
A comprehensive automated regression suite for the Trello REST API, designed to validate CRUD operations, state management, and edge cases using **Python** and **Pytest**. 
It simulates a realistic user journey: creating a board, managing lists, moving cards, and performing cleanup. These are all fully automated using a modular Page Object Model (POM) architecture and Dockerized execution.

## Tech Stack
* **Core:** Python (3.10+)
* **Framework:** Pytest
* **Containerization:** Docker 
* **Reporting:** pytest-html

## Architecture & Design Decisions
The framework is engineered to address common challenges in test automation through the following design choices:

* **Client-Test Separation:** All API interaction logic is encapsulated in `tests/api_client.py`. The test files (`tests/test_trello_api.py`) focus solely on assertions and business logic. This decoupling ensures that API changes only require updates in one location.
* **State Management via Fixtures:** Pytest fixtures (`tests/conftest.py`) handle the setup and teardown of test data. Every test run creates a fresh, isolated Board and guarantees its deletion after execution, preventing data pollution.
* **Containerization:** A `Dockerfile` is included to standardize the dependencies.
* **Visual Reporting:** This project runs automatically on every code change. You can verify the latest regression status and access the generated HTML reports by clicking the badge below (click on the *latest run*, then click the *Artifacts* tab):

[![Dockerized Python Tests](https://github.com/M7Shakeeb/Trello-Python-Automation/actions/workflows/docker-tests.yml/badge.svg)](https://github.com/M7Shakeeb/Trello-Python-Automation/actions/workflows/docker-tests.yml)

---

## Test Scenarios Covered

### Happy Path (CRUD Operations)
1.  **Lifecycle Management:** Automatic Board creation and deletion via Fixtures.
2.  **Workflow Validation:** Creates a "To-Do" & a "Done" lists, adds a Card, and moves it between lists to verify status updates.

### Negative & Edge Cases
1.  **Security:** Verifies that requests with Invalid Auth Tokens return `401 Unauthorized`.
2.  **Invalid Resources:** Verifies that requests for non-existent IDs (e.g., malformed or zeroed IDs) return `404 Not Found`.
3.  **Data Integrity:** Verifies that deleting a Board triggers a **Cascading Delete**, confirming that all child resources (Cards/Lists) are removed from the database.

---

## CI/CD Pipeline
A GitHub Actions workflow (`docker-tests.yml`) is configured to trigger on every push to the `main` branch. The pipeline performs the following steps:
1.  Builds the custom Docker Image.
2.  Injects secure credentials via GitHub Secrets.
3.  Executes the full regression suite inside the container.
4.  Uploads the generated HTML report as a build artifact.

---

## How to Run Locally

### Prerequisites
* Python 3.10+
* Docker (Optional, for containerized run)
* A Trello Account (Key & Token)(insert the credentials into **TRELLO_KEY** and **TRELLO_TOKEN** below respectively)

### Option 1: Direct Python Execution
Useful for rapid development and debugging.

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/M7Shakeeb/Trello-Python-Automation.git
    cd Trello-Python-Automation
    ```
2.  **Setup Virtual Environment:**
    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # Windows
    # source venv/bin/activate  # Mac/Linux
    ```
3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Secrets:**
    Create a `.env` file in the root directory:
    ```ini
    TRELLO_KEY=your_key_here
    TRELLO_TOKEN=your_token_here
    ```
5.  **Run Tests:**
    ```bash
    pytest --html=report.html
    ```

### Option 2: Docker Execution (Recommended)
Ensures the environment matches the CI server exactly.

1.  **Build the Image:**
    ```bash
    docker build -t trello-python-tests .
    ```
2.  **Run the Container:**
    (This command automatically injects your local `.env` variables into the container).
    ```bash
    docker run --rm --env-file .env trello-python-tests
    ```

---

## Project Structure
```text
Trello-Python-Automation/
├── .github/workflows/    # CI/CD Pipeline Definitions
├── tests/
│   ├── api_client.py     # API Abstraction Class (POM)
│   ├── conftest.py       # Shared Pytest Fixtures
│   └── test_trello_api.py # Test Suite
├── .dockerignore         # Build context optimization
├── Dockerfile            # Container definition
├── pytest.ini            # Test runner configuration
├── requirements.txt      # Python dependencies
└── README.md             # Documentation
```
## Author
**Shakeeb Mohammed**
* QA & Test Automation Engineer