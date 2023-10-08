"""
Program for generating quick pick lottery tickets
"""
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 45
NUMBER_OF_NUMBERS = 6


def main():
    number_of_picks = get_valid_number_of_picks()
    for i in range(number_of_picks):
        for j in range(NUMBER_OF_NUMBERS):
            print(generate_random_number(LOWER_LIMIT, UPPER_LIMIT))


def get_valid_number_of_picks():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 1:
        print("Invalid input.")
        number_of_picks = int(input("How many quick picks? "))
    return number_of_picks


main()
