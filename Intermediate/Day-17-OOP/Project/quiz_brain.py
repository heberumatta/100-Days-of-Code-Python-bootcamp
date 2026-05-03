class brain:
	def __init__(self):
		self.correct = 0
		self.questions_count = 0

	def ask(self, question):
			self.questions_count += 1
			printer = f'Q{self.questions_count}: {question.text} (True/False):'
			if question.answer == input(printer):
				self.correct += 1
				print('Thats correct!!')
			else:
				print('Thats wrong!!')
			print(f'Your score is: {self.correct}/{self.questions_count}.\n')


	def asking(self, question_bank):
		for question in question_bank:
			self.ask(question)
		print(f'\n\nYou`ve complete the quiz!!\n Your final score is {self.correct}/{self.questions_count}')
