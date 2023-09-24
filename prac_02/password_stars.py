"""
Program checking that a given password meets a minimum set length
and prints asterisks equal to the password's length.
"""


def main():
    minimum_length = 5
    password = get_valid_password(minimum_length)
    print("*" * len(password))


def get_valid_password(minimum):
    """Check that a password meets the minimum length."""
    password = input("Password: ")
    while len(password) < minimum:
        print(f"Password must be at least {minimum} characters.")
        password = input("Password: ")
    return password


main()
