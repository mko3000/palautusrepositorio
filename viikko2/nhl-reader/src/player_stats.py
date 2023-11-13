class PlayerStats:
    def __init__(self, players):
        self.players = players

    def top_scorers_by_nationality(self,nationality):
        filtered_players = []
        for player in self.players:
            if player.nationality == nationality:
                player.points = player.goals + player.assists
                filtered_players.append(player)

        return sorted(filtered_players, key=lambda p: p.points, reverse=True)