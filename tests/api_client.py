import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TrelloClient:
    def __init__(self):
        self.base_url = "https://api.trello.com/1"
        self.auth = {
            "key": os.getenv("TRELLO_KEY"),
            "token": os.getenv("TRELLO_TOKEN")
        }

    def create_board(self, name):
        url = f"{self.base_url}/boards"
        print(f"DEBUG: Connecting to {url}")  # <--- Added Debug Print
        params = {**self.auth, "name": name, "defaultLists": "false"}
        return requests.post(url, params=params)

    def get_board(self, board_id):
        url = f"{self.base_url}/boards/{board_id}"
        return requests.get(url, params=self.auth)

    def delete_board(self, board_id):
        url = f"{self.base_url}/boards/{board_id}"
        return requests.delete(url, params=self.auth)

    def create_list(self, board_id, name):
        url = f"{self.base_url}/lists"
        params = {**self.auth, "name": name, "idBoard": board_id}
        return requests.post(url, params=params)

    # --- NEW CARD FUNCTIONS ---
    def create_card(self, list_id, name):
        url = f"{self.base_url}/cards"
        params = {**self.auth, "name": name, "idList": list_id}
        return requests.post(url, params=params)

    def update_card(self, card_id, list_id):
        url = f"{self.base_url}/cards/{card_id}"
        params = {**self.auth, "idList": list_id}
        return requests.put(url, params=params)
    
    def get_card(self, card_id):
        url = f"{self.base_url}/cards/{card_id}"
        return requests.get(url, params=self.auth)