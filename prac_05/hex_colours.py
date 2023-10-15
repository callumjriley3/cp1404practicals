"""
Display hexadecimal code for a colour.
"""

COLOUR_TO_CODE = {"aliceblue": "#f0f8ff", "barnred": "#7c0a02", "cornflowerblue": "#6495ed", "daffodil": "#ffff31",
                  "emerald": "#50c878", "ferrarired": "#ff2800", "genericviridian": "#007f66",
                  "hollywoodcerise": "#f400a1", "internationalorange": "#ff4f00", "jonquil": "#f4ca16"}

colour = input("Enter colour name (without spaces): ").lower()
while colour != "":
    try:
        print(f"The hexadecimal code for {colour} is: {COLOUR_TO_CODE[colour]}")
    except KeyError:
        print("Invalid input.")
    colour = input("Enter colour name (without spaces): ").lower()
