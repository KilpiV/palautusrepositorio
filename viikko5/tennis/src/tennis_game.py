class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = [0, player1_name]
        self.player2 = [0, player2_name]

    def won_point(self, player_name):
        if self.player1[1] == player_name:
            self.player1[0] = self.player1[0]+ 1
        else:
            self.player2[0] = self.player2[0]+ 1

    def tied(self):
        score_prints = ["Love-All", "Fifteen-All", "Thirty-All", "Forty-All", "Deuce"]
        if self.player1[0] > 3:
            return score_prints[4]
        else:
            return score_prints[self.player1[0]]

    def four_or_more_points(self):
        leader = max(self.player1, self.player2)
        if abs(self.player1[0] - self.player2[0]) == 1:
            return "Advantage " + leader[1]
        else:
            return "Win for " + leader[1]
    
    def score_board(self):
        score_prints = ["Love", "Fifteen", "Thirty", "Forty"]
        return score_prints[self.player1[0]]+"-"+ score_prints[self.player2[0]]
    
    def get_score(self):
        if self.player1[0] == self.player2[0]:
            return self.tied()

        elif self.player1[0] >= 4 or self.player2[0] >= 4:
            return self.four_or_more_points()

        else:
            return self.score_board()
