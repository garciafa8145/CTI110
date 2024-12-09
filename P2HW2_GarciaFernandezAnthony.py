# Anthony Garcia-Fernandez
# 11/19/2024
# P2HW2: Grades Summary
# This program collects grades for six modules, stores them in a list, and displays the lowest grade, highest grade, sum, and average.

# Collect grades for six modules
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store grades in a list
module_grades = [module1, module2, module3, module4, module5, module6]

# Perform calculations
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

# Display results
print("\n------------Results------------")
print(f"Lowest Grade:       {lowest_grade:.2f}")
print(f"Highest Grade:      {highest_grade:.2f}")
print(f"Sum of Grades:      {sum_of_grades:.2f}")
print(f"Average:            {average_grade:.2f}")
print("-------------------------------")

