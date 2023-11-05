"""
Project Management Program
Estimated: 1 day
Actual:
"""
from prac_07.project import Project

MENU_TEXT = ("- (L)oad projects\n"
             "- (S)ave projects\n"
             "- (D)isplay projects\n"
             "- (F)ilter projects by date\n"
             "- (A)dd new project\n"
             "- (U)pdate project\n"
             "- (Q)uit")
DEFAULT_FILENAME = "projects.txt"
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_ESTIMATE_INDEX = 3
COMPLETION_PERCENTAGE_INDEX = 4


def main():
    projects = process_file(DEFAULT_FILENAME, COST_ESTIMATE_INDEX, COMPLETION_PERCENTAGE_INDEX)
    print(MENU_TEXT)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            new_filename = input("File name: ")
            projects = process_file(new_filename, COST_ESTIMATE_INDEX, COMPLETION_PERCENTAGE_INDEX)
        elif menu_selection == "S":
            pass
        elif menu_selection == "D":
            pass
        elif menu_selection == "F":
            pass
        elif menu_selection == "A":
            pass
        elif menu_selection == "U":
            pass
        else:
            print("Invalid selection.")
        print(MENU_TEXT)
        menu_selection = input(">>> ").upper()
    print("Thank you for using custom-built project management software.")


def process_file(filename, cost_estimate_index, completion_percentage_index):
    """Process data from file to store in a list."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # ignore headings
        for line in in_file:
            parts = line.strip().split("\t")
            parts[cost_estimate_index] = float(parts[cost_estimate_index])
            parts[completion_percentage_index] = float(parts[completion_percentage_index])
            projects.append(parts)
    return projects


main()
