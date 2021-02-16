# Guessing game

# Import the random package
import random


# Set a variable to store the best score
best_score = 100
record_holder = "Start"
# set a variable that sets whether to keep playing the game
keep_playing = True

# start the program
while keep_playing == True:
    # Set a boolean variable to keep guessing
    keep_asking = True

    # set the counter for number of guesses
    counter = 0
    # Set the number for the user to guess
    number = random.randint(1,100)

    # Start playing the guessing game
    print("Guess a number between 1 and 100")
    if best_score < 100:
        print("The current best score is {}, held by {}".format(best_score, record_holder))
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
    if counter < best_score:
        print("That's a new record! Congratulations!")
        best_score = counter
        name = input("Enter your name:")
        record_holder = name
    play_again = input("Play again? (y/n)")
    if play_again.lower() != "y":
        keep_playing = False