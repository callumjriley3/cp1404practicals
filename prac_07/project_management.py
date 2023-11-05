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
FILENAME = "projects.txt"


def main():
    print(MENU_TEXT)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            pass
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


main()
