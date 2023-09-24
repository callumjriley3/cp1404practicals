"""
Program to determine score status
"""
import random


def main():
    user_score = float(input("Enter score: "))
    result = determine_result(user_score)
    print(result)
    random_score = random.randint(0, 100)
    result = determine_result(random_score)
    print(f"Random score's result: {result}")


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


main()
