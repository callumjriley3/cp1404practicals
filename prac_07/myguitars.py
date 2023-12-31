"""
My Guitars
Guitar Program from Practical 7 Exercise
"""
from prac_07.guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Read guitars from file, store as list of Guitar objects and display sorted."""
    guitars = []
    with open(FILENAME, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            guitars.append(Guitar(parts[0], int(parts[1]), float(parts[2])))
    guitars.sort()
    for guitar in guitars:
        print(guitar)

    name = input("Guitar name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.")
        name = input("Guitar name: ")

    with open(FILENAME, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)


main()
