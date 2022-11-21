import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url

    def get_players(self):
        players_file = requests.get(self.url).json()
        players = []
        for player_dict in players_file:
            player = Player(player_dict['name'], player_dict['nationality'], player_dict['assists'], player_dict['goals'], player_dict['penalties'], player_dict['team'], player_dict['games'])
            players.append(player)

        return players
