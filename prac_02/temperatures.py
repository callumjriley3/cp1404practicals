"""
Program incorporating a menu to allow user to convert a temperature from
Celsius to Fahrenheit and from Fahrenheit to Celsius.
"""
MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_to_celsius(fahrenheit):
    """Calculate the equivalent of Fahrenheit temperature in Celsius."""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_to_fahrenheit(celsius):
    """Calculate the equivalent of Celsius temperature in Fahrenheit."""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()
