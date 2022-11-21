from player_reader import PlayerReader

def get_points(player):
    return player.get_points()

class PlayerStats:
    def __init__(self, PlayerReader):
        reader = PlayerReader

        self._players = reader.get_players()
        
    def top_scorers_by_nationality(self, nat):
        top_ones = []
        for player in self._players:
            if player.get_nationality() == nat:
                top_ones.append(player)
        top_ones.sort(key=get_points, reverse=True)
        return top_ones