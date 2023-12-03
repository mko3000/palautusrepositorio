from tennis_player import TennisPlayer

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = TennisPlayer(player1_name)
        self.player2 = TennisPlayer(player2_name)
        self.players = {
            player1_name: self.player1,
            player2_name: self.player2
        }

    def won_point(self, player_name):
        self.players[player_name].add_score()

    def get_score(self):
        winning_score = 4
        player1_score = self.player1.get_score()
        player2_score = self.player2.get_score()
        max_score = max(player1_score,player2_score)
        score_difference = abs(player1_score - player2_score)

        if self.get_leader() == None:
            if player1_score >= 3:
                score = "Deuce"
            else:
                score = f'{self.score_to_string(player1_score)}-All'
        elif max_score >= winning_score:            
            if score_difference == 1:
                score = f'Advantage {self.get_leader().get_name()}'
            else:
                score = f'Win for {self.get_leader().get_name()}'
        else:
            score = f'{self.score_to_string(player1_score)}-{self.score_to_string(player2_score)}'
        return score
    
    def get_leader(self):
        if self.player1.get_score() > self.player2.get_score():
            return self.player1
        elif self.player1.get_score() < self.player2.get_score():
            return self.player2
        return None
    
    def score_to_string(self,score:int) -> str:
        if score == 0:
            return "Love"
        if score == 1:
            return "Fifteen"
        if score == 2:
            return "Thirty"
        if score == 3:
            return "Forty"

    
