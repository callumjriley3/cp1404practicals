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
                champion = data[2]
                champion_to_number_of_wins[champion] = champion_to_number_of_wins.get(champion, 0) + 1
            if data[1] != "Country":
                countries.add(data[1])

    print("These 12 countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
