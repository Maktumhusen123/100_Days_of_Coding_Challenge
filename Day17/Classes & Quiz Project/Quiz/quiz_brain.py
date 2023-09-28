
class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # TODO 1: Asking the questions
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {current_question.text} True/False: ")
        self.check_answer(answer.lower(), current_question.answer.lower())

    def still_has_question(self):
        return self.question_number < len(self.question_list)

# TODO 2 : Checking if the answer was correct
    def check_answer(self, answer, correct_answer):
        if answer == correct_answer:
            self.score += 1
            print(f"Your score is {self.score}")
        else:
            print("That's wrong")
        print(f"The Correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")



# TODO 3 : Checking if we are end of the quiz
