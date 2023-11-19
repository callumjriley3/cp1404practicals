"""
CP1404 Practical 9
Test the SilverServiceTaxi class.
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def run_tests():
    """Run a series of tests to demonstrate the SilverServiceTaxi class's methods."""
    my_silver_service_taxi = SilverServiceTaxi("Prius 2", 100, 2)
    my_silver_service_taxi.drive(18)
    print("Expected fare: $48.80")
    print(f"Fare output: ${my_silver_service_taxi.get_fare()}")
    print(my_silver_service_taxi)


run_tests()
