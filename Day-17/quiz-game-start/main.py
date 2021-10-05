from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    q_text = question['question']
    q_answer = question['correct_answer']
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
total_question = len(question_bank)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"You've completed the quiz. \n"
      f"Your final score was: {quiz.score}/{quiz.question_number}")

