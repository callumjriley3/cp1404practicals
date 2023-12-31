"""
Project Management Program
Estimated: 1 day
Actual: 426 minutes
"""
from prac_07.project import Project
import datetime

MENU_TEXT = ("- (L)oad projects\n"
             "- (S)ave projects\n"
             "- (D)isplay projects\n"
             "- (F)ilter projects by date\n"
             "- (A)dd new project\n"
             "- (U)pdate project\n"
             "- (Q)uit")
DEFAULT_FILENAME = "projects.txt"


def main():
    """Allow for a file to be loaded or saved to, display and filter the projects, and also add or update projects."""
    projects = process_file(DEFAULT_FILENAME)
    print(MENU_TEXT)
    menu_selection = input(">>> ").upper()
    while menu_selection != "Q":
        if menu_selection == "L":
            new_filename = input("File name: ")
            try:
                projects = process_file(new_filename)
            except FileNotFoundError:
                print(f"Could not find file {new_filename}")
        elif menu_selection == "S":
            new_filename = input("File name: ")
            write_to_file(projects, new_filename)
        elif menu_selection == "D":
            display_projects(projects)
        elif menu_selection == "F":
            filter_by_date(projects)
        elif menu_selection == "A":
            print("Let's add a new project")
            new_project = get_new_project()
            projects.append(new_project)
        elif menu_selection == "U":
            projects = update_project(projects)
            print(projects)
        else:
            print("Invalid selection.")
        print(MENU_TEXT)
        menu_selection = input(">>> ").upper()
    write_to_file(projects, DEFAULT_FILENAME)
    print("Thank you for using custom-built project management software.")


def display_projects(projects):
    """Display projects grouped based on completion percentage."""
    projects.sort()
    print("Incomplete projects:")
    for project in projects:
        if project.completion_percentage < 100.0:
            print(project)
    print("Completed projects:")
    for project in projects:
        if project.completion_percentage == 100.0:
            print(project)


def process_file(filename):
    """Process data from file to store in a list of objects."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # ignore headings
        for line in in_file:
            parts = line.strip().split("\t")
            projects.append(Project(parts[0], parts[1], int(parts[2]), float(parts[3]), float(parts[4])))
    return projects


def write_to_file(projects, filename):
    """Save data to a file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def filter_by_date(projects):
    """Filter list of projects when given a date."""
    filtered_projects = []
    user_date_string = input("Show projects that start after date (dd/mm/yy): ")
    is_valid_date = False
    while not is_valid_date:
        try:
            user_date = datetime.datetime.strptime(user_date_string, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date.")
            user_date_string = input("Show projects that start after date (dd/mm/yy): ")

    for project in projects:
        formatted_start_date = datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
        if formatted_start_date >= user_date:
            filtered_projects.append(project)
    filtered_projects.sort()
    for filtered_project in filtered_projects:
        print(filtered_project)


def get_new_project():
    """Get details for a new project."""
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yy): ")
    is_valid_date = False
    while not is_valid_date:
        try:
            formatted_start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date.")
            start_date = input("Start date (dd/mm/yy): ")
    priority = int(input("Priority: "))
    cost_estimate = float(input("Cost estimate: $"))
    completion_percentage = float(input("Percent complete: "))
    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    return new_project


def update_project(projects):
    """Update details of a project"""
    for i, project in enumerate(projects):
        print(i, project)
    project_selection = int(input("Project choice: "))
    print(projects[project_selection])
    updated_percentage = float(input("New Percentage: "))
    if updated_percentage != "":
        projects[project_selection].completion_percentage = updated_percentage
    updated_priority = int(input("New Priority: "))
    if updated_priority != "":
        projects[project_selection].priority = updated_priority
    return projects


main()
