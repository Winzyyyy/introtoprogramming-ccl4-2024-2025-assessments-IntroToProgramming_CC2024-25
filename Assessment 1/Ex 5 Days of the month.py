monthDays = {
        1: 31,  
        2: 28,
        3: 31 ,        #Months and days stored in a Dictionary.
        4: 30 , 
        5: 31 , 
        6: 30 , 
        7: 31 , 
        8: 31 , 
        9: 30 , 
        10: 31 , 
        11: 30 , 
        12: 31
}
months = int(input("Enter the month number (1-12): ")) #asking the user using an integer input.
if 1 <= months <= 12:    #using if's 
    if months == 2:   #if months is 2 
         leapYear = input("Is it a Leap Year (y/n): ") #user input when declaring 2  
         if leapYear == "y":
              print("We have a Leap Year which is 29 days.")
         else:
              print("its only 28 days.")
    else:
     print(f"{monthDays[months]} days")
else:
     print("Please enter a valid month number")   
  