from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, All, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players.txt"
    reader = PlayerReader(url)

    stats = Statistics(reader)

    query = QueryBuilder()

    print("---\n")
    def printPlayers(matcher):
        for player in stats.matches(matcher):
            print(player)
        print("\n---\n")

    query = QueryBuilder()
    #matcher = query.playsIn("NYR").hasFewerThan(1,"goals").build()
    #matcher = query.playsIn("NYR").build()
    # matcher = (
    #     query
    #     .playsIn("NYR")
    #     .hasAtLeast(10, "goals")
    #     .hasFewerThan(20, "goals")
    #     .build()
    # )

    m1 = (
        query
            .playsIn("PHI")
            .hasAtLeast(10, "assists")
            .hasFewerThan(5, "goals")
            .build()
        )

    m2 = (
        query
            .playsIn("EDM")
            .hasAtLeast(50, "points")
            .build()
        )

    matcher = query.oneOf(m1, m2).build()

    printPlayers(m1)
    printPlayers(m2)
    printPlayers(matcher)

   


if __name__ == "__main__":
    main()
