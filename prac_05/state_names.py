"""
CP1404/CP5632 Practical
State names in a dictionary
"""

MAX_SHORT_STATE_LENGTH = 3
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

for pair in CODE_TO_NAME.items():
    print(f"{pair[0]:{MAX_SHORT_STATE_LENGTH}} is {pair[1]}")


state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
