class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1_score = 0
        self.p2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.p1_score = self.p1_score + 1
        else:
            self.p2_score = self.p2_score + 1

    def get_score(self):
        score = ""
        match_length_before_overtime = 4
        scorelist = {0: "Love", 1: "Fifteen", 2: "Thirty", 3: "Forty"}

        if self.p1_score == self.p2_score:
            if self.p1_score <= 3:
                score = scorelist[self.p1_score] + "-All"
            else:
                score = "Deuce"
        elif self.p1_score >= match_length_before_overtime or self.p2_score >= match_length_before_overtime:
            p2_lead = self.p1_score - self.p2_score
            if p2_lead == 1:
                score = "Advantage player1"
            elif p2_lead == -1:
                score = "Advantage player2"
            elif p2_lead >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            score = scorelist[self.p1_score] + "-" + scorelist[self.p2_score]

 

        return score
