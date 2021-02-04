# Blood donor program

# Set constants
MIN_AGE = 16
MIN_WEIGHT = 50

# Get age and weight of user
age = int(input("What is your age?"))
weight = int(input("How much do you weigh in kg?"))

# Check if they are eligible
if age >= MIN_AGE and weight >= MIN_WEIGHT:
    print("You are eligible to donate blood")
else:
    print("You are not eligible")