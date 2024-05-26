import util as util
from questions import Question

#this is accessing util.py and asinging a variable 
questions = util.questions 
answers = util.answers
options = util.options

#created this list to append and store the user answers
guesses = []

#this is a variable with the value of 0 to keep score
score = 0

#variable to keep track of questions answered by user
#on file util.py/Question line 18 to 24 first it checks if
#answer is correct and then sums one point to score and adds 1 number to
#question_num so it can iterate to the question list
question_num = 0

#Object used to call the class Question and does a method call which calls the
#list as arguments from util.py  
question = Question()
#here it calls the fucntion def resolveTest and we are able to pass the arguments 
#called answers questions and options
guesses, score, question_num = question.resolveTest(questions,answers,options) 
"""for question in questions:
    print("--------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else: 
        print("Incorrect")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
    """

#Added some decoration for the quiz using prints
print("--------------------")
print("------RESULTS-------")
print("--------------------")

#this ode block will print the word Answers and iterate over the answers list
print("ANSWERS: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

#this ode block will print the word Guesses and iterate over the guesses list we created
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

#this will divide the score by the total number of questions ahd then multiply it by 100
#to get the percentage then its going to convert it an integer and ´print it
score = int(score / len(questions) * 100.0)
print(f"your Score is {score}% ")
