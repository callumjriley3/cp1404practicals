"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    A ValueError will occur when the input is not an integer.
2. When will a ZeroDivisionError occur?
    A ZeroDivisionError will occur if the user inputs 0 as the denominator.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    The error could be avoided by adding a while loop to ensure that denominator is not zero.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator must not be 0.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
