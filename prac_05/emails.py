"""
Emails
Estimate: 20 minutes
Actual:
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        full_name = extract_name(user_email)
        selection = input(f"Is your name {full_name}? (Y/n) ")
        user_email = input("Email: ")


def extract_name(user_email):
    parts = user_email.split("@")
    names = parts[0].split(".")
    full_name = " ".join(names).title()
    return full_name


main()
