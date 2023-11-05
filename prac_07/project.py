"""
Project Class
"""


class Project:
    """Represent a Project."""

    def __init__(self, name="", start_date="01/01/0001", priority=0, cost_estimate=0.0, completion_percentage=0.0):
        """Construct a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string according to format."""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")
