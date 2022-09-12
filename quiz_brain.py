class QuizBrain:
    def __init__(self, q_list):
        """
        A simple Command line quiz app written in python
        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number <= self.question_list.index(self.question_list[-1])

    def next_question(self):
        question = self.question_list[self.question_number]
        user_answer = input(f"Q.{self.question_number + 1}: {question.text} True/False: ")
        correct_answer = question.answer
        self.check_answer(user_answer, correct_answer)
        self.question_number += 1

    def check_answer(self, i_answer, c_answer):
        if i_answer == c_answer:
            self.score += 1
            print("You are right!")
        else:
            print('Wrong Answer!')
        print(f'The correct answer was:{c_answer}')
        print(f'Your current score is:{self.score}/{self.question_number + 1}')

    def get_result(self):
        if not self.still_has_questions():
            print(f"You've Completed the quiz your got: {self.score}/{self.question_number} ")
