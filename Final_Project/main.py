import matplotlib.pyplot as plt

class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.current_question_index = 0

    def display_question(self):
        question = self.questions[self.current_question_index]
        print(question.prompt)
        user_answer = input("Enter your answer: ")
        self.check_answer(user_answer)

    def check_answer(self, user_answer):
        question = self.questions[self.current_question_index]
        if user_answer.lower() == question.answer.lower():
            self.score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {question.answer}")
        self.current_question_index += 1

    def has_more_questions(self):
        return self.current_question_index < len(self.questions)

    def display_score(self):
        print(f"Your final score is {self.score} out of {len(self.questions)}")
        self.plot_score()

    def plot_score(self):
        labels = ['Correct Answers', 'Wrong Answers']
        correct = self.score
        wrong = len(self.questions) - self.score
        counts = [correct, wrong]

        plt.bar(labels, counts, color=['green', 'red'])
        plt.xlabel('Result')
        plt.ylabel('Number of Questions')
        plt.title('Quiz Results')
        plt.show()

question_prompts = [
    "What is the capital of France?\n(a) Paris\n(b) London\n(c) Rome\n(d) Berlin\n",
    "What is the largest planet in our solar system?\n(a) Earth\n(b) Jupiter\n(c) Mars\n(d) Saturn\n",
    "Who wrote 'To Kill a Mockingbird'?\n(a) Harper Lee\n(b) Mark Twain\n(c) J.K. Rowling\n(d) Ernest Hemingway\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "a")
]

def run_quiz():
    quiz = Quiz(questions)
    while quiz.has_more_questions():
        quiz.display_question()
    quiz.display_score()

if __name__ == "__main__":
    run_quiz()

























"""from quiz import Question

def main():
    prompt = input("Enter the question prompt")

    options = []

    num_options = int(input("how many are they? "))

from Final_Project.quizEN import QuestionEnglish

def main():
    prompt = input("Enter the question prompt: ")
    
    options = []
    num_options = int(input("How many options are there? "))
    for i in range(num_options):
        option = input(f"Enter option {i + 1}: ")
        options.append(option)
    
    answer = input("Enter the correct answer: ")

    # Create an instance of the Question class
    question = QuestionEnglish(prompt, options, answer)

    # Display the question and options to the user
    print("\n" + question.prompt)
    for idx, option in enumerate(question.options):
        print(f"{idx + 1}. {option}")

    # Get the user's answer and check if it is correct
    user_answer = input("Enter your answer: ")
    if question.is_correct(user_answer):
        print("Correct!")
    else:
        print("Incorrect. The correct answer is:", question.answer)

if __name__ == "__main__":
    main()"""