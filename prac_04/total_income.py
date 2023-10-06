"""
CP1404/CP5632 Practical
Code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    total = 0
    print_report(incomes, number_of_months, total)


def print_report(incomes, number_of_months, total):
    """Print income report with income total for each month."""
    print("\nIncome Report\n-------------")
    for month in range(number_of_months):
        income = incomes[month]
        total += income
        print("Month {:2} - Income: ${:10.2f}         Total: ${:10.2f}".format(month, income, total))


main()
