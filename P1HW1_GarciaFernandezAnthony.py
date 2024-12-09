# Your Name: Anthony Garcia-Fernandez
# Date: 10/14/24
# Assignment Name: P1HW1
# A brief description of the project: This program takes a base and an exponent from the user, calculates the power, and performs some arithmetic operations with three integers provided by the user.

# Getting base and exponent from the user
base = int(input("Enter the base value: "))
exponent = int(input("Enter the exponent value: "))

# Calculating the result
result = base ** exponent

# Displaying the power calculation result
print(f"{base} raised to the power of {exponent} is {result}!")

# Getting three integers from the user
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))

# Performing addition and subtraction
sum_of_first_two = num1 + num2
final_result = sum_of_first_two - num3

# Displaying the final result
print(f"The sum of {num1} and {num2} is {sum_of_first_two}.")
print(f"Subtracting {num3} gives {final_result}.")
d
