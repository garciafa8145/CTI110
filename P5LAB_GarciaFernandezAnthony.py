#Anthony Garcia-Fernandez
#11/19/2024
#P5LAB
#This program simulates a self-checkout machine. It calculates the change owed to the customer
#and displays the denominations required to return the change.

import random

def disperse_change(change):
    """
    This function calculates the denominations of change owed in dollars, quarters, dimes, nickels, and pennies.
    It prints out the required quantities of each.
    """
    # Denominations in cents
    denominations = {"dollars": 100, "quarters": 25, "dimes": 10, "nickels": 5, "pennies": 1}
    change_in_cents = int(round(change * 100))  # Convert change to cents for accurate calculations

    print("Change breakdown:")
    for denomination, value in denominations.items():
        count = change_in_cents // value
        change_in_cents %= value
        print(f"{denomination.capitalize()}: {count}")

def main():
    # Generate a random total owed (between $0.01 and $100.00)
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"Total owed: ${total_owed:.2f}")

    # Prompt the user for the cash amount entered
    cash_entered = float(input("Enter the amount of cash you will put into the machine: $"))
    
    while cash_entered < total_owed:
        print("Insufficient cash. Please enter an amount greater than or equal to the total owed.")
        cash_entered = float(input("Enter the amount of cash you will put into the machine: $"))
    
    # Calculate the change
    change = round(cash_entered - total_owed, 2)
    print(f"Change owed: ${change:.2f}")

    # Call the disperse_change function
    disperse_change(change)

# Run the program
if __name__ == "__main__":
    main()
