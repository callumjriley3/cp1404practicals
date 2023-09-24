"""
Program checking that a given password meets a minimum set length
and prints asterisks equal to the password's length.
"""


def main():
    minimum_length = 5
    password = get_password(minimum_length)
    print_stars(password)


def print_stars(password):
    """Print the number of stars equal to the password length."""
    print("*" * len(password))


def get_password(minimum_length):
    """Return a password that meets the minimum length."""
    password = input("Password: ")
    while len(password) < minimum_length:
        print(f"Password must be at least {minimum_length} characters.")
        password = input("Password: ")
    return password


main()
