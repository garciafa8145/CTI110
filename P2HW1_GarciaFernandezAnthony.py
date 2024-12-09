# Your Name: Anthony Garcia-Fernandez
# Date: 10/14/2024
# Assignment Name: P2HW1
# A brief description of the project: This program calculates and displays the travel budget with proper formatting for destination and expenses.

# Get user inputs
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("Enter amount spent on gas: "))
accommodation = float(input("Enter amount spent on accommodation: "))
food = float(input("Enter amount spent on food: "))

# Calculate total expenses
total_expenses = gas + accommodation + food
remaining_budget = budget - total_expenses

# Display results
print("\nTravel Budget Summary")
print("----------------------")
print(f"{'Destination:':<25} {destination}")
print(f"{'Budget:':<25} ${budget:.2f}")
print(f"{'Gas:':<25} ${gas:.2f}")
print(f"{'Accommodation:':<25} ${accommodation:.2f}")
print(f"{'Food:':<25} ${food:.2f}")
print(f"{'Total Expenses:':<25} ${total_expenses:.2f}")
print(f"{'Remaining Budget:':<25} ${remaining_budget:.2f}")
