from tests.api_client import TrelloClient

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