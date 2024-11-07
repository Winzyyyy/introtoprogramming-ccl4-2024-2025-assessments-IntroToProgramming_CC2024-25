capital = input("What is the Capital of France? : ") #asking the user 
if capital.lower() == "paris": #case sensitive
     print("Correct")
else:
     print("Wrong! The correct answer is Paris")

questions = {
        "What is the capital of France?": "paris",
        "What is the capital of Germany?": "berlin",
        "What is the capital of Italy?": "rome",
        "What is the capital of Spain?": "madrid",          #Lists of the Countries and its Capitals
        "What is the capital of Portugal?": "lisbon",        #dictionary
        "What is the capital of Belgium?": "brussels",
        "What is the capital of Netherlands?": "amsterdam",
        "What is the capital of Greece?": "athens",
        "What is the capital of Switzerland?": "bern",
        "What is the capital of Austria?": "vienna",
    }

for question, correct_answer in questions.items():  #key-value
        user_answer = input(question + " ").strip().lower()    #case sensitive 
        if user_answer == correct_answer: 
            print("Correct!")
        else:
            print("Wrong. The correct answer is:", correct_answer.capitalize()) 
