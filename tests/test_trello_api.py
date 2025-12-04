import pytest
import random
from tests.api_client import TrelloClient

# Initialize the client
client = TrelloClient()

@pytest.fixture(scope="module")
def board_id():
    """Setup: Create board -> Yield ID -> Teardown: Delete board"""
    # 1. Setup
    board_name = f"Python-Frame-Board-{random.randint(1000, 9999)}"
    response = client.create_board(board_name)
    assert response.status_code == 200
    
    board_id = response.json()["id"]
    print(f"\n[SETUP] Created Board: {board_id}")
    
    yield board_id
    
    # 2. Teardown
    del_response = client.delete_board(board_id)
    assert del_response.status_code == 200
    print(f"\n[TEARDOWN] Deleted Board: {board_id}")

def test_get_board_details(board_id):
    response = client.get_board(board_id)
    assert response.status_code == 200
    assert response.json()["id"] == board_id

def test_create_list_on_board(board_id):
    list_name = "Python To-Do List"
    response = client.create_list(board_id, list_name)
    
    assert response.status_code == 200
    assert response.json()["name"] == list_name
    assert response.json()["idBoard"] == board_id

# --- NEGATIVE TESTS ---

def test_invalid_auth_returns_401(board_id):
    """Verify that using a bad token returns 401 Unauthorized"""
    # We temporarily break the client's auth
    original_token = client.auth["token"]
    client.auth["token"] = "INVALID_TOKEN_123"
    
    response = client.get_board(board_id)
    
    # Restore the token immediately so we don't break other tests!
    client.auth["token"] = original_token
    
    assert response.status_code == 401

def test_get_non_existent_board_returns_404():
    """Verify that fetching a fake ID returns 404 Not Found"""
    fake_id = "000000000000000000000000" # 24 zeros
    response = client.get_board(fake_id)
    
    assert response.status_code == 404