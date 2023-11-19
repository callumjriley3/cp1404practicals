"""
CP1404 Practical 9 - Taxi Simulator
Estimated: 40 minutes
Actual: 28 minutes
"""

from prac_09.silver_service_taxi import SilverServiceTaxi
from prac_09.taxi import Taxi

MENU_TEXT = "q)uit, c)hoose taxi, d)rive"


def main():
    bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    print("Let's drive!")
    print(MENU_TEXT)
    menu_selection = input(">>> ").lower()
    while menu_selection != "q":
        if menu_selection == "c":
            print("Taxis available:")
            display_taxis(taxis)
            current_taxi = get_valid_taxi_selection(current_taxi, taxis)
        elif menu_selection == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill = drive_taxi(bill, current_taxi)
        else:
            print("Invalid option")
        print(f"Bill to date: ${bill:.2f}")
        print(MENU_TEXT)
        menu_selection = input(">>> ").lower()
    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def drive_taxi(bill, current_taxi):
    distance = float(input("Drive how far? "))
    current_taxi.drive(distance)
    print(f"Your {current_taxi.name} trip cost you ${current_taxi.get_fare():.2f}")
    bill += current_taxi.get_fare()
    return bill


def get_valid_taxi_selection(current_taxi, taxis):
    taxi_selection = int(input("Choose taxi: "))
    try:
        current_taxi = taxis[taxi_selection]
    except IndexError:
        print("Invalid taxi choice")
    except ValueError:
        print("Invalid taxi choice")
    return current_taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()
