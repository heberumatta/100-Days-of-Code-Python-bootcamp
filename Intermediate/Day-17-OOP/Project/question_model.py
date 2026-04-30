from data import question_data
import random

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

class QuestionBank:
    def __init__(self, questions):
        self.question_bank = []
        for question in questions:
            self.question_bank.append(Question(question["text"], question["answer"]))
        random.shuffle(self.question_bank)
