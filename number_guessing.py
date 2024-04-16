# Author: Mishti Gala
# Email: mishtikalpes@umass.edu
# Date: 1st November 2023

# Import the 'random' module to generate a random number.
import random

# Prompt the user to input the upper limit for the range of numbers to guess from.
top_of_range = input("Type a number: ")

# Check if the input is a digit (a valid number).
if top_of_range.isdigit():
    # Convert the input to an integer if it's a digit.
    top_of_range = int(top_of_range)
    
    # Check if the integer is less than or equal to 0.
    if top_of_range <= 0:
        # Print an error message and exit the program if the input is not a valid range.
        print('Please type a number larger than 0 next time.')
        quit()
else:
    # Print an error message and exit the program if the input is not a valid number.
    print('Please type a number next time.')
    quit()

# Generate a random number within the range of 0 to the user-specified upper limit.
random_number = random.randint(0, top_of_range)

# Initialize a variable to keep track of the number of guesses.
guesses = 0

# Start an infinite loop for the guessing game.
while True:
    # Increment the number of guesses made.
    guesses += 1
    
    # Prompt the user to make a guess.
    user_guess = input("Make a guess: ")
    
    # Check if the user's input is a digit (a valid number).
    if user_guess.isdigit():
        # Convert the user's input to an integer if it's a digit.
        user_guess = int(user_guess)
    else:
        # Print an error message and continue the loop if the input is not a valid number.
        print('Please type a number next time.')
        continue

    # Compare the user's guess with the randomly generated number.
    if user_guess == random_number:
        # Print a message indicating that the user has guessed the correct number.
        print("You got it!")
        # Exit the loop if the guess is correct
        break
    elif user_guess > random_number:
        # Print a message indicating that the user's guess is above the random number.
        print("You were above the number!")
    else:
        # Print a message indicating that the user's guess is below the random number.
        print("You were below the number!")

# Print the final message with the number of guesses it took to guess the correct number.
print("You got it in", guesses, "guesses")
