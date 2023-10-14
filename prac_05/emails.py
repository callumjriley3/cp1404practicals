"""
Emails
Estimate: 20 minutes
Actual:
"""


def main():
    email_to_name = {}
    user_email = input("Email: ")
    while user_email != "":
        name = extract_name(user_email)
        print(name)
        user_email = input("Email: ")


def extract_name(user_email):
    parts = user_email.split("@")
    name = parts[0].split(".")
    return name


main()
