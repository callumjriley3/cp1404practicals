"""
Emails
Estimate: 20 minutes
Actual: 45 minutes
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
    print()
    for pair in email_to_name.items():
        print(f"{pair[1]} ({pair[0]})")


def extract_name(email):
    parts = email.split("@")
    names = parts[0].split(".")
    full_name = " ".join(names).title()
    return full_name


main()
