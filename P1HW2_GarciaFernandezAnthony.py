# Your Name: Anthony Garcia-Fernandez
# Date: 2024-10-14
# Assignment Name: P1HW2
# A brief description of the project: This program calculates travel expenses based on user input and checks if they are within budget.

# Asking the user for their budget
budget = float(input("Enter your budget for the trip: "))

# Asking the user for their travel destination
destination = input("Enter your travel destination: ")

# Asking the user for expenses
gas_expense = float(input("Enter amount you will spend on gas: "))
accommodation_expense = float(input("Enter amount you will spend on accommodation: "))
food_expense = float(input("Enter amount you will spend on food: "))

# Adding up expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtracting total expenses from budget
remaining_budget = budget - total_expenses

# Displaying results
print(f"\nTravel Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")

# Checking if within budget
if remaining_budget >= 0:
    print("You are within your budget!")
else:
    print("You are over your budget!")
