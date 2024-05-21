from quizEN import QuestionEnglish
from quizES import QuestionSpanish

results = []
question1 = QuestionSpanish("Cuanto es 2 + 2? \n",[1,2,3,4],4)
user_response1 = int(input("type the correct number \n") )
results.append({'question': "Cuanto es 2 + 2 ? \n", 'user_response' : user_response1, 'is_correct' : question1.is_correct(user_response1)})

question2 = QuestionSpanish("En que pais esta ubicada la ciudad de Barcelona? \n", ["Mexico","Brasil","España","Honduras"],"España")
user_response2 = input("Escribe el pais correcto!\n")
results.append({'question': "En que pais esta ubicada la ciudad de Barcelona? \n", 'user_response' : user_response2, 'is_correct': question2.is_correct(user_response2)})







for result in results:
    print("Question:", result['question'])
    print("User Response:", result['user_response'])
    print("Is Correct:", result['is_correct'])
    print()



























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