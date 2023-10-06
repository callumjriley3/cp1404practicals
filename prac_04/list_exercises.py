"""Program for various list exercises."""


def main():
    """Get input for 5 numbers and store them in a list to print the first, last, min, max, and average."""
    numbers = []
    for i in range(5):
        number = float(input("Number: "))
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    username = get_username()
    access_status = determine_status(username, usernames)
    print(f"Access {access_status}")


def get_username():
    """Return a username obtained from user"""
    username = input("Username: ")
    return username


def determine_status(username, usernames):
    """Return status (granted or denied) based on list of existing usernames."""
    if username in usernames:
        return "granted"
    else:
        return "denied"


main()
