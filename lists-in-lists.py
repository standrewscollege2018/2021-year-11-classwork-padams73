# This program demonstrates lists inside lists
# Called multi-dimensional arrays

# In this list, each sub-list contains the name and age
people = [["Dr Evil", 45], ["Gru", 34], ["Emperor", 200]]

# Get new person details
keep_asking = True
while keep_asking == True:
    # Set up a smaller list called person to hold the new details being entered
    person = []
    name = input("Name:")
    # If the user enters 'end' as their name it breaks out of the loop
    if name == "end":
        keep_asking = False
    else:
        age = input("Age:")
        # Add the new name and age to the sub-list called person
        person.append(name)
        person.append(age)
        # Append the person list to the bigger people list
        people.append(person)

# To print a sub-list:
print(people[0])

# To print items in a sub-list:
for i in range(len(people)):
    print("{} is {} years old".format(people[i][0], people[i][1]))

#######################
# Add functionality where the user can input a new name and age for a person
# This is then added to the people list
# Which is then printed out at the end