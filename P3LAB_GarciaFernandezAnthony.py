# P3LAB_Garcia-Fernandeez
# This program calculates the optimal number of dollars, quarters, dimes, nickels, and pennies for a given float value representing money.

def main():
    # Input: amount of money
    money = float(input("Enter an amount of money (e.g., 12.34): "))
    
    # Convert to cents to avoid dealing with decimals
    total_cents = int(money * 100)

    # If no money is entered
    if total_cents == 0:
        print("No money entered.")
        return

    # Calculate the number of each coin type
    dollars = total_cents // 100
    total_cents %= 100

    quarters = total_cents // 25
    total_cents %= 25

    dimes = total_cents // 10
    total_cents %= 10

    nickels = total_cents // 5
    total_cents %= 5

    pennies = total_cents

    # Output results
    if dollars > 0:
        print(f"{dollars} dollar{'s' if dollars > 1 else ''}")

    if quarters > 0:
        print(f"{quarters} quarter{'s' if quarters > 1 else ''}")

    if dimes > 0:
        print(f"{dimes} dime{'s' if dimes > 1 else ''}")

    if nickels > 0:
        print(f"{nickels} nickel{'s' if nickels > 1 else ''}")

    if pennies > 0:
        print(f"{pennies} penn{'ies' if pennies > 1 else 'y'}")

if __name__ == "__main__":
    main()
