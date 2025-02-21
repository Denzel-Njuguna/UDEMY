from questions import questions
import random

class Question:
    def __init__(self):
        self.points = 0
        self.text = None
        self.answer = None
        self.user_answer = None
        self.asked_question = []
    def check_question_asked(self,index):
        if index in self.asked_question:
            self.get_question()
        else:
            self.asked_question.append(index)
        
    def get_question(self):
        selected_key = random.choice(list(questions.keys()))
        self.check_question_asked(str(selected_key))
        selected_question = list(questions[selected_key].keys())[0]
        selected_answer = list(questions[selected_key].values())[0]

        self.text = selected_question
        self.answer = selected_answer

        self.user_answer = input(f"{self.text}\n").capitalize().strip()
        self.check_answer()
    def check_answer(self):
        if self.answer == self.user_answer:
            self.points+=1
            print(f"correct your points are {self.points}")
            self.get_question()
        else:
            print(f"incorrect the answer is {self.answer} and your tally points are {self.points}")
# random choice only works in tuples and lists




