"""
Guitar class
Estimated: 20 minutes
Actual:
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
