import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def __new__(cls, url):
        cls.url = url
        return cls.get_players(cls)

    def get_players(self):
        """Returns a list of Player objects"""
        response = requests.get(self.url, timeout=100).json()
        players = []
        for player_dict in response:
            player = Player(player_dict)
            players.append(player)
        return players
    