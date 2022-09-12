from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = list()

for i in question_data:
    question_bank.append(Question(i['question'], i['correct_answer']))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    question = quiz_brain.next_question()

quiz_brain.get_result()
