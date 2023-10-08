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
        random_numbers = []
        for j in range(NUMBER_OF_NUMBERS):
            random_number = generate_random_number(LOWER_LIMIT, UPPER_LIMIT)
            while random_number in random_numbers:
                random_number = generate_random_number(LOWER_LIMIT, UPPER_LIMIT)
            random_numbers.append(random_number)
            random_numbers.sort()
        print(" ".join(f"{random_number:2}" for random_number in random_numbers))


def get_valid_number_of_picks():
    number_of_picks = int(input("How many quick picks? "))
    while number_of_picks < 1:
        print("Invalid input.")
        number_of_picks = int(input("How many quick picks? "))
    return number_of_picks


def generate_random_number(lower_limit, upper_limit):
    return random.randint(lower_limit, upper_limit)


main()
