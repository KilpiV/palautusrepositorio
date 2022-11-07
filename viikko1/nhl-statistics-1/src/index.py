from statistics import Statistics
from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def main():
    stats = Statistics(
    PlayerReader())

    # järjestetään kaikkien tehopisteiden eli maalit+syötöt perusteella
    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)
        
    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)
#    player = PlayerReader()
 #   stats = Statistics(player)
  #  philadelphia_flyers_players = stats.team("PHI")
   # top_scorers = stats.top(10)

#    print("Philadelphia Flyers:")
 #   for player in philadelphia_flyers_players:
  #      print(player)
#
 #   print("Top point getters:")
  #  for player in top_scorers:
   #     print(player)


if __name__ == "__main__":
    main()
