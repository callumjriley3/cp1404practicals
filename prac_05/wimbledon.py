"""
Wimbledon
Estimate: 50 minutes
Actual: 42 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Process data from file and display champions, number of wins and winning countries."""
    champion_to_number_of_wins = {}
    countries = set()
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            data = line.split(",")
            if data[2] != "Champion":
                add_to_dictionary(champion_to_number_of_wins, data)
            if data[1] != "Country":
                countries.add(data[1])

    display_champions(champion_to_number_of_wins)
    print()
    display_countries(countries)


def add_to_dictionary(champion_to_number_of_wins, data):
    """Add champion name and how many times a win for that champion occurs to dictionary."""
    champion = data[2]
    champion_to_number_of_wins[champion] = champion_to_number_of_wins.get(champion, 0) + 1


def display_champions(champion_to_number_of_wins):
    """Print each champion and their number of wins."""
    print("Wimbledon Champions: ")
    for pair in champion_to_number_of_wins.items():
        print(f"{pair[0]} {pair[1]}")


def display_countries(countries):
    """Print winning countries in alphabetical order."""
    print("These 12 countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
