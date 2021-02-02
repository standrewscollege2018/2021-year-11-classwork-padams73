# This program doubles a number entered by the user

# If an input is an integer, we wrap the input in int()
# By default the input is text, so we must do this
number = int(input("Enter a number"))

# If the number will have a decimal, it is a float
decimal_number = float(input("Enter a decimal"))

print(number * 2)

print(decimal_number * 2)