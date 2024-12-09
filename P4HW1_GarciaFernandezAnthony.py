# Anthony Garcia-Fernandez
# Date: 11/10/2024
# Assignment: P4HW1 - Score Validation and Grade Calculation
# Description: This program collects a specified number of scores, validates them,
#              removes the lowest score, calculates an average, and assigns a letter grade.

# Step 1: Ask the user for the number of scores they want to enter.
num_scores = int(input("Enter the number of scores you would like to enter: "))

# Step 2: Initialize an empty list to store valid scores.
scores = []

# Step 3: Use a loop to get scores, validate each one, and add it to the list if valid.
for i in range(num_scores):
    # Loop to ensure valid score entry
    while True:
        score = float(input(f"Enter score #{i + 1}: "))  # Prompt user for score
        if 0 <= score <= 100:
            scores.append(score)  # Add valid score to the list
            break
        else:
            print("Invalid score. Please enter a score between 0 and 100.")  # Error message for invalid score

# Step 4: Calculate results after collecting all valid scores.
lowest_score = min(scores)             # Find the lowest score
scores.remove(lowest_score)             # Remove the lowest score from the list
average_score = sum(scores) / len(scores)  # Calculate average of remaining scores

# Step 5: Determine the letter grade based on the average.
if average_score >= 90:
    letter_grade = 'A'
elif average_score >= 80:
    letter_grade = 'B'
elif average_score >= 70:
    letter_grade = 'C'
elif average_score >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

# Step 6: Display the results to the user.
print(f"\nLowest score: {lowest_score}")
print("Modified List:", scores)
print(f"Scores Average: {average_score:.2f}")
print(f"Letter Grade: {letter_grade}")
