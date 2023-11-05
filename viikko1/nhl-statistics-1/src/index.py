from statistics_service import StatisticsService, SortBy
from player_reader import PlayerReader


def main():
    stats = StatisticsService(PlayerReader("https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"))
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)
    #top_goal_scorers = stats.top(3, "GOALS")
    #top_assist_scorers = stats.top(3, "ASSISTS")

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)

    top_goal_scorers = stats.top(4, SortBy.GOALS)
    print("Top goal scorers:")
    for player in top_goal_scorers:
        print(player)

    top_assist_scorers = stats.top(4, SortBy.ASSISTS)
    print("Top assist scorers:")
    for player in top_assist_scorers:
        print(player)


if __name__ == "__main__":
    main()
