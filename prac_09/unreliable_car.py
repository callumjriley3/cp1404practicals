"""
CP1404 Practical 9
UnreliableCar Class
"""
from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that includes reliability"""

    def __init__(self, name, fuel, reliability):
        """Initialise a Taxi instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return f"{super().__str__()}"

    def drive(self, distance):
        """Drive like parent Car depending on reliability"""
        if random.randrange(0, 101) < self.reliability:
            super().drive(distance)
        else:
            super().drive(0)
        return distance
