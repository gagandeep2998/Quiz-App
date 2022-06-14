class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        question_text = current_question.text
        question_answer = current_question.answer
        user_ans = input(f"Q.{self.question_number}: {question_text} (True/False)?: ")
        self.check_answer(user_ans, question_answer)

    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            print("You're right!")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}")




