# This program asks the user for three names
# It appends them to a list and then prints them out

# names list will store the entered names
names = []

# Now we loop 3 times, asking for names and appending them
for i in range(3):
    name = input("Enter name: ")
    names.append(name)

# Print the final list by looping through iter
for n in names:
    print(n)
