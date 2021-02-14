# Example of a while loop
keep_asking = True

while keep_asking == True:
    name = input("Enter your name:")
    if name == "Henry":
        keep_asking = False
    else:
        print("Wrong name")
print("Hi Henry")