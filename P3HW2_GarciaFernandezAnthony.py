# Anthony Garcia-Fernandez
# 10-28-24
# P3HW2
# This program calculates an employee's gross pay including overtime if applicable.

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))


if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0


regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay


print("\nEmployee Pay Summary")
print("---------------------------------------------------------")
print(f"{'Employee Name':<15}{'Pay Rate':<10}{'Hours Worked':<15}{'Overtime Hours':<15}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
print("---------------------------------------------------------")
print(f"{employee_name:<15}{pay_rate:<10.2f}{hours_worked:<15.2f}{overtime_hours:<15.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<15.2f}")
