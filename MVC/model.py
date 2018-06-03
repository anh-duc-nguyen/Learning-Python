class Model:
	"""docstring for Model"""
	def __init__(self):
		self.ans = 0
	def setAns(self, ans):
		self.ans = ans
	def getAns(self):
		return self.ans

	def add(self, first , second):
		self.ans = first + second
	def sub(self, first , second):
		self.ans = first - second
	def mul(self, first , second):
		self.ans = first * second
	def div(self, first , second):
		self.ans = first / second
	
