import pytest
import random
from tests.api_client import TrelloClient

@pytest.fixture(scope="module")
def client():
    """Provides a shared TrelloClient instance for all tests."""
    return TrelloClient()

@pytest.fixture(scope="module")
def board_id(client):
    """Setup: Create board -> Yield ID -> Teardown: Delete board."""
    board_name = f"Trello-Automation-Board-{random.randint(100, 999)}"
    response = client.create_board(board_name)
    assert response.status_code == 200
    
    board_id = response.json()["id"]
    print(f"\n[SETUP] Created Board: {board_id}")
    
    yield board_id
    
    # Teardown
    client.delete_board(board_id)
    print(f"\n[TEARDOWN] Deleted Board: {board_id}")

@pytest.fixture(scope="module")
def lists(client, board_id):
    """Creates To-Do and Done lists for card workflow tests."""
    resp_todo = client.create_list(board_id, "To-Do")
    assert resp_todo.status_code == 200
    
    resp_done = client.create_list(board_id, "Done")
    assert resp_done.status_code == 200
    
    return {"todo": resp_todo.json()["id"], "done": resp_done.json()["id"]}