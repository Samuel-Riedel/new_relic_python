class Question():

    def _init__(self):
        pass
    
    def resolveTest(self,questions,answers,options):
        score = 0
        question_num = 0
        guesses = []
        for question in questions:
            print("--------------------")
            print(question)
            for option in options[question_num]:
                print(option)

            guess = input("Enter (A, B, C, D): \n").upper()
            guesses.append(guess)
            if guess == answers[question_num]:
                score += 1
                print("Correct!")
            else: 
                print("Incorrect")
                print(f"{answers[question_num]} is the correct answer")
            question_num += 1
        return guesses, score, question_num