"""Band class for CP1404 Practical 9"""
from prac_09.musician import Musician


class Band:
    """Band class for storing members of a band."""

    def __init__(self, name):
        """Initialise band."""

        self.name = name
        self.band_members = []

    def __str__(self):
        """Return string representation of a Band."""
        return f"{self.name} ({', '.join(str(band_member) for band_member in self.band_members)})"

    def add(self, musician):
        """Add musician to the Band."""
        self.band_members.append(musician)

    def play(self):
        """Return a string displaying the band member and the first (or no) instrument they play."""
        band_member_strings = [band_member.play() for band_member in self.band_members]
        return '\n'.join(band_member_strings)
