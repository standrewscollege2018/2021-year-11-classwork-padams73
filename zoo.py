# Zoo program
# Start by setting a constant
# This is the age limit for a child
CHILD_AGE = 13
# Get the age of the user
age = int(input("What is your age?"))

# Check if they are a child
if age < CHILD_AGE:
    print("You pay the child price")

print("Welcome to the zoo")