# 🐍 Trello API Automation (Python Framework)

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Framework-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)

## 📄 Project Overview
This project demonstrates a **modular, scalable API automation framework** built from scratch using Python.

Unlike standard linear scripting, this framework utilizes the **Client-Test Separation pattern** (similar to Page Object Model) to decouple the HTTP request logic from the test assertions. This ensures high maintainability and reusability.

## 🛠️ Tech Stack
* **Language:** Python
* **HTTP Client:** `requests` library
* **Test Runner:** `pytest`
* **Security:** `python-dotenv` for environment variable management

## 📂 Architecture
* **`tests/api_client.py`:** A reusable class that encapsulates all Trello API endpoints. It handles authentication and base URLs automatically.
* **`tests/test_trello_api.py`:** The actual test suite using Pytest fixtures for Setup (Create Board) and Teardown (Delete Board).

## 🧪 Scenarios Covered
1.  **Lifecycle Management:** Automatic Board creation and cleanup via Pytest Fixtures.
2.  **CRUD Operations:** Creating Lists, Creating Cards, Moving Cards.
3.  **Negative Testing:** Validating error handling for Invalid Auth (401) and Invalid IDs (404).

## 🚀 How to Run
1.  **Clone the repo:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Trello-Python-Automation.git](https://github.com/YOUR_USERNAME/Trello-Python-Automation.git)
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure Secrets:**
    Create a `.env` file in the root directory:
    ```ini
    TRELLO_KEY=your_key
    TRELLO_TOKEN=your_token
    BASE_URL=[https://api.trello.com/1](https://api.trello.com/1)
    ```
4.  **Run Tests:**
    ```bash
    pytest
    ```