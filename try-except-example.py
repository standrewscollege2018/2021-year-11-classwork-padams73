# Example of try and except

keep_asking = True

while keep_asking == True:
    try:
        number = int(input("Enter integer"))
        print("You chose", number)
        keep_asking = False
    except:
        print("That's not an integer!")

print("**** All done ****")