# This program runs a raffle

# Import random so we can select a winner
import random
# Import time so we can build tension with a pause
import time

# Set list to store names of people in raffle
names = []

# Greeting the user
print("Welcome to the big raffle!")

# Get the prize details
get_prize = True
while get_prize == True:
    prize = input("What is the prize being raffled? ")
    if len(prize) == 0:
        print("You must enter something")
    else:
        get_prize = False
get_value=True
while get_value == True:
    try:
        value = float(input("What is the value of the {}? $".format(prize)))
        get_value = False
    except:
        print("Enter a number")

# Now, get the names for the raffle
get_names = True
while get_names == True:
    name = input("Enter name: ")
    if name.lower() == "end":
        get_names = False
    else:
        names.append(name)

# Before selecting a winner, we need to check that the list isn't empty
if len(names) == 0:
    print("No people entered the raffle")
else:
    winner = random.randint(0,len(names))
    print("The winner of the {}, worth ${}, is...".format(prize, value))
    time.sleep(2)
    print("...{}! Congratulations!".format(names[winner]))
