#Here we create the class called Question
class Question():

    def __init__(self): #this will initiate the method init with the argument self
        pass
    
#the fucntion below will iterate over questions list and check if the answer is correct
#it will compare the answer from the user using the variable with appended answers called "guesses"
#if the answer is correct it will add 1 point to the variable "score" and store it to the variable
# if the user gives the wrong answer it will iterate over the list and sum 1 value to the
#variable question_num so it can keep track of the current question and then  go to the next question,
#it will also print the correct answer in the terminal 
    def resolveTest(self,questions,answers,options):
        score = 0
        question_num = 0
        guesses = []
        for question in questions:
            print("--------------------")
            print(question)
            for option in options[question_num]:
                print(option)

            guess = input("Enter (A, B, C, D): \n").upper() #this input will let the user answer the question and the answer will converted to lower case
            guesses.append(guess) #this is appending the answer to the variable guess
            if guess == answers[question_num]:
                score += 1
                print("Correct!")
            else: 
                print("Incorrect")
                print(f"{answers[question_num]} is the correct answer")
            question_num += 1
        return guesses, score, question_num
#the return statement will send us the variables so we can use them in the main.py function