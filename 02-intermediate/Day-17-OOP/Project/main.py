from question_model import QuestionBank
from data import question_data
from quiz_brain import brain

question_bank = QuestionBank(question_data).question_bank

quiz = brain()
quiz.asking(question_bank)

