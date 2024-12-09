# Anthony Garcia-Fernandez
# 11/23/2024
# Assignment: P5HW - Math Quiz
# Description: A program that generates simple math quizzes, provides feedback on answers, 
# and keeps track of the number of guesses until the user gets the correct answer.

import random

def addition_quiz():
    """
    Generates two random numbers for an addition problem.
    Asks the user to guess the answer and provides feedback until correct.
    Tracks the number of guesses.
    """
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 + num2
    guess_count = 0

    print(f"\nSolve this problem:\n{num1}\n+ {num2}")

    while True:
        try:
            user_guess = int(input("Enter your answer: "))
            guess_count += 1
            if user_guess == correct_answer:
                print(f"Congratulations! You got it right!")
                print(f"It took you {guess_count} guesses.")
                break
            elif user_guess < correct_answer:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def subtraction_quiz():
    """
    Generates two random numbers for a subtraction problem.
    Asks the user to guess the answer and provides feedback until correct.
    Tracks the number of guesses.
    """
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    correct_answer = num1 - num2
    guess_count = 0

    print(f"\nSolve this problem:\n{num1}\n- {num2}")

    while True:
        try:
            user_guess = int(input("Enter your answer: "))
            guess_count += 1
            if user_guess == correct_answer:
                print(f"Congratulations! You got it right!")
                print(f"It took you {guess_count} guesses.")
                break
            elif user_guess < correct_answer:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """
    Main program that provides a menu-driven interface for the math quiz.
    """
    while True:
        print("\nMAIN MENU")
        print("1. Addition Quiz")
        print("2. Subtraction Quiz")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            addition_quiz()
        elif choice == "2":
            subtraction_quiz()
        elif choice == "3":
            print("Thank you for playing! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Run the program
if __name__ == "__main__":
    main()
