names = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]  #Lists
findName = input("Enter the name to search for: ") #user input
if findName in names: #using if and in to check if the user input is in the Lists
    print(f"{findName} was found in the list.")
else:
    print(f"{findName} was not found in the list.")






