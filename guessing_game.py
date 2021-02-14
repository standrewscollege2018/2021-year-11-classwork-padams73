# Guessing game

# Import the random package
import random

# Set a boolean variable to keep the program running
keep_asking = True
# set the counter for number of guesses
counter = 0
# Set the number for the user to guess
number = random.randint(1,100)

# Start guessing
print("Guess a number between 1 and 100")
while keep_asking == True:
    # add one to the counter
    counter += 1

    guess = int(input("Guess a number:"))
    if guess == number:
        keep_asking = False
    elif guess > number:
        print("Too high. Guess lower")
    else:
        print("Too low. Guess higher")
# Loop has finished, they must have guessed the number
print("That's right!")
print("You took {} guesses".format(counter))
