"""
Program for generating quick pick lottery tickets
"""
import random

LOWER_LIMIT = 1
UPPER_LIMIT = 45
NUMBER_OF_NUMBERS = 6


def main():
    number_of_picks = get_number_of_picks()
    for i in range(number_of_picks):
        for j in range(NUMBER_OF_NUMBERS):
            print(generate_random_number(LOWER_LIMIT, UPPER_LIMIT))


main()