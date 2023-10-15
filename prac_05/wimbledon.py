"""
Wimbledon
Estimate: 50 minutes
Actual:
"""

FILENAME = "wimbledon.csv"


def main():
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
    champion = data[2]
    champion_to_number_of_wins[champion] = champion_to_number_of_wins.get(champion, 0) + 1

def display_champions(champion_to_number_of_wins):
    print("Wimbledon Champions: ")
    for pair in champion_to_number_of_wins.items():
        print(f"{pair[0]} {pair[1]}")

def display_countries(countries):
    print("These 12 countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
