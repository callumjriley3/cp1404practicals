"""
CP1404 Practical 9
Test the UnreliableCar class.
"""
from prac_09.unreliable_car import UnreliableCar


def run_tests():
    """Run a series of tests to demonstrate UnreliableCar class' methods and reliability attribute."""
    my_unreliable_car = UnreliableCar("Old Jeep", 100, 0)
    my_unreliable_car.drive(20)
    print("Expected output: Old Jeep, fuel=100, odometer=0")
    print(my_unreliable_car)
    my_reliable_car = UnreliableCar("New Car", 100, 100)
    my_reliable_car.drive(20)
    print("Expected output: New Car, fuel=80, odometer=20")
    print(my_reliable_car)


run_tests()
