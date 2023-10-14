"""
Emails
Estimate: 20 minutes
Actual:
"""


def main():
    email_to_name = {}
    email = input("Email: ")
    while email != "":
        full_name = extract_name(email)
        selection = input(f"Is your name {full_name}? (Y/n) ").upper()
        if selection != "Y" and selection != "":
            full_name = input("Name: ")
        email_to_name[email] = full_name
        email = input("Email: ")


def extract_name(email):
    parts = email.split("@")
    names = parts[0].split(".")
    full_name = " ".join(names).title()
    return full_name


main()
