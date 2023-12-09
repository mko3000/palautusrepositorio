from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    def printPlayers(matcher):
        for player in stats.matches(matcher):
            print(player)
        print("\n---\n")


    matcher1 = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(20, "assists"),
        PlaysIn("PHI")
    )

    matcher2 = And(
        Not(HasAtLeast(2, "goals")),
        PlaysIn("NYR")
    )

    matcher3 = And(
        HasFewerThan(1, "assists"),
        HasAtLeast(1, "goals"),        
        PlaysIn("NYR"),
        All()
    )

    print("---\n")
    printPlayers(matcher1)
    printPlayers(matcher2)
    printPlayers(matcher3)

    filtered_with_all = stats.matches(All())
    print(len(filtered_with_all))




if __name__ == "__main__":
    main()
