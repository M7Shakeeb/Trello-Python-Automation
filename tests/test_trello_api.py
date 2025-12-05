from tests.api_client import TrelloClient
import random

# Happy Path Testing

def test_get_board_details(client, board_id):
    """Verify board can be retrieved by ID"""
    response = client.get_board(board_id)
    
    assert response.status_code == 200
    assert response.json()["id"] == board_id


def test_card_workflow(client, lists):
    """
    Full lifecycle of the Card:
    1. Create Card in To-Do List
    2. Move Card to Done List
    """
    # 1. Create Card
    card_name = "Sign-Up for Trello"
    create_resp = client.create_card(lists["todo"], card_name)
    
    assert create_resp.status_code == 200
    card_id = create_resp.json()["id"]
    assert create_resp.json()["idList"] == lists["todo"]
    
    # 2. Move Card to Done
    move_resp = client.update_card(card_id, lists["done"])
    
    assert move_resp.status_code == 200
    assert move_resp.json()["idList"] == lists["done"]

# Negative Testing

def test_invalid_auth_returns_401(board_id):
    """Verify that using a bad token returns 401 Unauthorized"""
    # We create a fresh client instance so we don't break the main 'client' fixture
    bad_client = TrelloClient()
    # Manually break the token in the auth dictionary
    bad_client.auth["token"] = "INVALID_TOKEN_123"
    
    response = bad_client.get_board(board_id)
    
    assert response.status_code == 401

def test_get_non_existent_board_returns_404(client):
    """Verify that fetching a fake ID returns 404 Not Found"""
    fake_id = "000000000000000000000000"
    response = client.get_board(fake_id)
    
    assert response.status_code == 404

# Verifying that Trello performs a Cascading Delete (i.e., when a parent object is deleted, the children die with it).

def test_delete_board_cascades_to_card(client):
    """
    Scenario: Create Board -> Add List -> Add Card -> Delete Board -> Check Card
    Expected: Card should return 404 (Not Found) because parent board is gone.
    """
    # 1. Create a dedicated board for this test
    board_name = f"Negative-Test-Board-{random.randint(100, 999)}"
    board_resp = client.create_board(board_name)
    board_id = board_resp.json()["id"]
    
    # 2. Add List and Card
    list_resp = client.create_list(board_id, "Temporary List")
    list_id = list_resp.json()["id"]
    
    card_resp = client.create_card(list_id, "Ghost Card")
    card_id = card_resp.json()["id"]
    
    # 3. Delete the Board
    client.delete_board(board_id)
    
    # 4. Verify the Card is gone
    response = client.get_card(card_id)
    assert response.status_code == 404
