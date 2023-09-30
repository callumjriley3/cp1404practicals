"""
Demonstrate multiple instances of reading and writing to files.
"""


# 1.
FILENAME = "name.txt"

name = input("Name: ")
out_file = open(FILENAME, "w")
print(name, file=out_file)
out_file.close()

# 2.
FILENAME = "name.txt"  # Constant defined again "as if it were a separate program."

in_file = open(FILENAME, "r")
for line in in_file:
    print(f"Your name is {line}")
in_file.close()

# 3.
FILENAME = "numbers.txt"

in_file = open(FILENAME, "r")
value_one = int(in_file.readline())
value_two = int(in_file.readline())
in_file.close()
print(f"The sum of these two digits is: {value_one + value_two}")

# 4.1
FILENAME = "numbers.txt"

total = 0
in_file = open(FILENAME, "r")
for line in in_file:
    total += int(line)
in_file.close()
print(f"The total of these numbers is: {total}")
