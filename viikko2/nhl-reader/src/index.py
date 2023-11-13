import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    response = requests.get(url).json()

    # print("JSON-muotoinen vastaus:")
    # print(response)

    players = []

    for player_dict in response:
        player = Player(player_dict)
        players.append(player)

    print("Players from FIN\n")

    fin_players = []
    for player in players:
        if player.nationality == "FIN":
            player.points = player.goals + player.assists
            fin_players.append(player)

    fin_players = sorted(fin_players, key=lambda p: p.points, reverse=True)
    for player in fin_players:       
        print(player)

if __name__ == "__main__":
    main()
