"""
Guitar class
Estimated: 20 minutes
Actual: 23 minutes
"""


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string according to format."""
        return f"{self.name} ({self.year}) : ${self.cost}"

    def get_age(self):
        age = 2022 - self.year  # using year specified in exercise
        return age

    def is_vintage(self):
        return 2022 - self.year >= 50
