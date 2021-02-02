# This program is a Madlib, getting the user to enter details
# then it prints out a story

print("Welcome to my Madlib program!")
# Get their details

body_part = input("Enter a body part:")
name = input("Enter a name:")
# Print the story
print("Hello {}, you have the strangest looking {} I have ever seen".format(name, body_part))