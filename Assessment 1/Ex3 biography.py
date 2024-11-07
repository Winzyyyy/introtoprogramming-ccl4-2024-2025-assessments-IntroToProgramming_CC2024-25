name = input("Enter your name: ")
hometown = input("Enter your hometown: ")

while True:             #whileTrue is to continue the loop
    age_input = input("Enter your age: ")
    try:     #try lets you test a code of errors
        age = int(age_input)
        break       #break exits you to loop
    except :    #except lets you handle errors
        print("Plesse enter a valid number")

details = {"name": name, "hometown": hometown,"age": age}      #keyvalue
print(f"Name: {details['name']}, Hometown: {details['hometown']}, Age: {details['age']}")  
