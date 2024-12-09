# Your Name: Anthony Garcia-Fernandez
# Date: 10/14/2024
# Assignment Name: P2LAB1
# A brief description of the project: This program calculates the diameter, circumference, and area of a circle based on the radius input by the user.

import math

# Get the radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * (radius ** 2)

# Display the results formatted to specified decimal places
print(f"Diameter: {diameter:.1f}")
print(f"Circumference: {circumference:.2f}")
print(f"Area: {area:.3f}")
