"""
CP1404 Practical
Test the Taxi class.
"""
from prac_09.taxi import Taxi


def run_tests():
    """Run a series of tests to demonstrate the Taxi class' methods."""
    my_taxi = Taxi("Prius 1", 100)

    my_taxi.drive(40)

    print(my_taxi)

    my_taxi.start_fare()
    my_taxi.drive(100)

    print(my_taxi)


run_tests()
