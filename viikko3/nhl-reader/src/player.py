class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nat = nationality
        self.assi = assists
        self.goal = goals
        self.pena = penalties
        self.team = team
        self.games = games
        self.point = assists+goals
    
    def get_points(self):
        return self.point

    def get_nationality(self):
        return self.nat
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goal:3} +{self.assi:3} ={self.point:3}"
        #return f"{self.name:24} team {self.team} goal {self.goal:3} assists {self.assi}"
