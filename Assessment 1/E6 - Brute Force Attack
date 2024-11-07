attempts = 5  #number of attempts
count = 0    
while count < attempts: #while attempts are greater than count
    Passcode = int(input("Enter your Passcode: ")) #user input using integers
    correct_passcode = 12345 #declaring the correct passcode
    if Passcode == correct_passcode: #passcode matches the correct_passcode
        print("You have Entered the Correct Password")
        break #breaking the while loop
    else:
        count +=1 
        countLeft = attempts - count #subtracting the attempts if incorrect passcode is entered
        print(f"Incorrect Passcode! You have {countLeft} attempts left.") #displays the attempts left
if attempts == count:
   print("You have reached the maximum attempts. Authorities have been alerted!")
