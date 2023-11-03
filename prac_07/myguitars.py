"""
My Guitars
Guitar Program from Practical 7 Exercise
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"
NAME_INDEX = 0
YEAR_INDEX = 1
COST_INDEX = 2


def main():
    """Read guitars from file, store as list of Guitar objects and display sorted."""
    with open(FILENAME, 'r') as in_file:
        guitars = []
        for line in in_file:
            parts = line.strip().split(',')

            name = parts[NAME_INDEX]
            year = parts[YEAR_INDEX]
            cost = parts[COST_INDEX]
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    name = input("Guitar name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Guitar name: ")

    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
