from question_model import Question
from data import question_data
from quiz_brain import QuizBrain



question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/ {quiz.question_number}")

"""participants = ['Participant 1', 'Participant 2' ]  # Sample participants
scores = quiz.score  # Sample quiz scores

plt.bar(participants, scores)
plt.xlabel(len(question_bank))
plt.ylabel('Scores')
plt.title('Quiz Scores')
plt.show()"""