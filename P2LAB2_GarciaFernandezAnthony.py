# Your Name: Anthony Garcia-Fernandez
# Date: 10/14/2024
# Assignment Name: P2LAB2
# A brief description of the project: This program creates a dictionary of vehicles and their MPG ratings, allowing users to calculate the gas needed for a specified number of miles.

# Create a dictionary with vehicle MPG values
vehicle_mpg = {
    "Camaro": 18.21,
    "Prius": 52.36,
    "Model S": 110,
    "Silverado": 26
}

# Get the keys from the dictionary
keys = vehicle_mpg.keys()
# Print the keys
print("Available vehicles:", list(keys))

# Prompt the user to enter a vehicle
user_vehicle = input("Enter the vehicle name (exactly as shown): ")

# Check if the vehicle is in the dictionary
if user_vehicle in vehicle_mpg:
    # Display the MPG for the vehicle
    print(f"{user_vehicle} MPG: {vehicle_mpg[user_vehicle]}")
    
    # Prompt the user for miles driven
    miles = float(input("Enter the number of miles you will drive: "))
    
    # Calculate gallons needed
    mpg = vehicle_mpg[user_vehicle]
    gallons_needed = miles / mpg
    
    # Display the gallons needed, rounded to two decimal places
    print(f"Gallons of gas needed: {gallons_needed:.2f}")
else:
    print("Vehicle not found. Please check the name and try again.")
