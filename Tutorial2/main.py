import util as util
from questions import Question

questions = util.questions
answers = util.answers
options = util.options

guesses = []

score = 0

question_num = 0

question = Question()
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


print("--------------------")
print("------RESULTS-------")
print("--------------------")

print("ANSWERS: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100.0)
print(f"your Score is {score}% ")
