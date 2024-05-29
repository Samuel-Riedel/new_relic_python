import util as util
import matplotlib.pyplot as plt
import json
from questions import Question
from writeJSON import append_data_to_file

#this is accessing util.py and asinging a variable 
questions = util.questions 
answers = util.answers
options = util.options

#asks the user to create a username to save it on JSON file
username = input("Create your username: \n")

#variable saves in an input the gender of the person  and sends its to the json file in lower case
gender= input("Please specify a gender\nMale\nFemale\nOthers\n").lower()

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

#this code block will print the word Guesses and iterate over the guesses list we created
print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

#this will divide the score by the total number of questions ahd then multiply it by 100
#to get the percentage then its going to convert it an integer and ´print it
score = int(score / len(questions) * 100.0)
print("-------------------------")
print(f"--| your Score is {score}% |--")
print("-------------------------")


#JSON import
if __name__ == "__main__":
    file = "C:/Users/samue/OneDrive/Escritorio/Migracode/new_relic_python/Final_Project/points.json"
    new_data = {"username": username, "gender": gender, "score": score}
    append_data_to_file(file, new_data)
#Loading JSON
with open('C:/Users/samue/OneDrive/Escritorio/Migracode/new_relic_python/Final_Project/points.json') as f:
    data = json.load(f)

#Comprenhension lists with json data
users = [entry.get("username","unknown") for entry in data["points"]]
scores = [entry.get("score", 0)for entry in data["points"]]
genders = [entry.get("gender","unknown")for entry in data["points"]]

#Variable with medium scores for plot
int_result = int(''.join(map(str, scores))) #stackoverflow convert list to numbers, i dont know why i created this variable, not going to delete it might use it later
medium_score = sum(scores) / len(users) #tried to sum a list and divide it by length of list, now its fixed with sum(score) 


#Matplotlib part
plt.plot(users,scores)
plt.plot(medium_score)
plt.xlabel("Usernames")
plt.ylabel("Scores")
plt.title("Quiz Scores")

plt.legend(["Score"])
plt.show()

#-------------------------------------------------------------------------------------------------------------------------------------------
#testing part
#print(users)
#print(scores)
##print(genders)
print("-----------------------")
print(f"-Average Score: {round(medium_score,2)}%-")
print("-----------------------")
print()

############################################################################
                                   #TODO LIST                              
#1)crear un subplot de genders y                                           #
#  scores para ver que gender tiene mejores scores                         #
#                                                                          #
#2) agregar un ID al JSON por cada user nuevo                              #
#                                                                          #
#3) Arreglar lo del path en la variable "file" de la linea 75              #
# de main.py,tiene que ser un nombre corto y no todo el path del archivo   #
#                                                                          #
#                                                                          #
#4) Investigar si el json file lo puedo ordenar para sacar los top 10      #
#   mejores resultados y compararlos en matplotlib                         #
#                                                                          #
#5) crear validation de users para que no hayan nombres repitdos           #
#                                                                          #
#6) cambiar las preguntas del JSON sean mas facil de leer                  #                                                                        #
############################################################################