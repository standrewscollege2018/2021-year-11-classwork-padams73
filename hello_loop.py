# This program says hello to people

# Find out how many people there are
number = int(input("How many names will you enter?"))


# Start loop to say  hello
for i in range(1,number+1):

    name = input("{}. What is your name?".format(i))
    print("Hello", name)

print("All done. Goodbye")