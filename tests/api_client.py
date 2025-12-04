import requests
import os
from dotenv import load_dotenv

# Load env variables once when this module is imported
load_dotenv()

class TrelloClient:
    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.auth = {
            "key": os.getenv("TRELLO_KEY"),
            "token": os.getenv("TRELLO_TOKEN")
        }

    def create_board(self, name):
        url = f"{self.base_url}/boards"
        params = {**self.auth, "name": name}
        response = requests.post(url, params=params)
        return response

    def get_board(self, board_id):
        url = f"{self.base_url}/boards/{board_id}"
        response = requests.get(url, params=self.auth)
        return response

    def delete_board(self, board_id):
        url = f"{self.base_url}/boards/{board_id}"
        response = requests.delete(url, params=self.auth)
        return response

    def create_list(self, board_id, name):
        url = f"{self.base_url}/lists"
        params = {**self.auth, "name": name, "idBoard": board_id}
        response = requests.post(url, params=params)
        return response