"""
Guitar Test
"""

from prac_06.guitar import Guitar


def run_tests():
    first_guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    print(f"{first_guitar.name} get_age() - Expected 100. Got {first_guitar.get_age()}")
    second_guitar = Guitar("Another Guitar", 2013, 0)
    print(f"{second_guitar.name} get_age() - Expected 9. Got {second_guitar.get_age()}")


run_tests()
