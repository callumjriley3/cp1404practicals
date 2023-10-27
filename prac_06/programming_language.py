"""Programming language class."""


class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name="", typing="", reflection=True, year=0):
        """Initialise ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine if programming language is dynamic."""
        return self.typing == "Dynamic"
