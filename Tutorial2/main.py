questions = ("Cuanto es 1 + 1? ",
             "Cuantos es 2 + 2? ",
             "Cuantos es 2 + 2? ",
             "Cuantos es 2 + 2? ",
             "Cuantos es 2 + 2? ",
             )

options = (("A. 2 ", "B. 3 ", "C. 5 ", "D. 7 "),
           ("A. 2 ", "B. 3 ", "C. 5 ", "D. 7 "),
           ("A. 4 ", "B. 6 ", "C. 8 ", "D. 10 "),
           ("A. 6 ", "B. 8 ", "C. 10 ", "D. 12 "),
           ("A. 10 ", "B. 11 ", "C. 12 ", "D. 13 "))

answers = ("A","B","B","D","A")
guesses = []

score = 0

question_num = 0

for question in questions:
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

score = int(score / len(questions) * 100)
print(f"your Score is {score}% ")