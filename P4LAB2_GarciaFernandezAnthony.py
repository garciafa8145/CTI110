

# Anthony Garcia-Fernandez
# CTI 110 - P4LAB2
# Multiplication Table Program
# Date: November 19, 2024
# This program prompts the user to enter an integer and displays its multiplication table (1 to 12).
# It continues to prompt the user until they decide to exit.

while True:
    # Prompt the user to enter an integer
    number = int(input("Enter an integer: "))

    # Check if the number is negative
    if number < 0:
        print("This program does not handle negative numbers.")
    else:
        # Display the multiplication table using a for loop
        for i in range(1, 13):
            print(f"{number} * {i} = {number * i}")

    # Ask if the user wants to run the program again
    repeat = input("Would you like to run the program again? (yes/no): ").strip().lower()
    if repeat != "yes":
        print("Exiting program...")
        break
