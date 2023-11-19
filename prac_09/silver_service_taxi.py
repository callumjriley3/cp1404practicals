"""
CP1404 Practical 9
SilverServiceTaxi class
"""
from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Create a subclass of Taxi that includes fanciness"""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string like a Taxi but with flagfall stated."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def start_fare(self):
        """Begin a new fare."""
        super().start_fare()

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + self.flagfall

