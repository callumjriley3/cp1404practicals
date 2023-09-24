"""
Program using a menu to get a valid score, print a result and print stars.
"""
LOWER_LIMIT = 0
UPPER_LIMIT = 100
MENU = """
    (G)et Score
    (P)rint Result
    (S)how Stars
    (Q)uit
    """


def main():
    score = get_valid_score()
    print(MENU)
    option = input(">>> ").upper()
    while option != "Q":
        if option == "G":
            score = get_valid_score()
        elif option == "P":
            result = determine_result(score)
            print(result)
        elif option == "S":
            show_stars(score)
        else:
            print("Invalid input.")
        print(MENU)
        option = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    """Return a score from lower limit to upper limit, inclusive."""
    score = float(input("Score: "))
    while score < LOWER_LIMIT or score > UPPER_LIMIT:
        print("Invalid score.")
        score = float(input("Score: "))
    return score


def determine_result(score):
    """Return a different result depending on the value of the score."""
    if score > 100 or score < 0:
        result = "Invalid score"
    elif score >= 90:
        result = "Excellent"
    elif score >= 50:
        result = "Passable"
    else:
        result = "Bad"
    return result


def show_stars(score):
    """Print the number of stars equal to the score as an integer."""
    print("*" * int(score))


main()
