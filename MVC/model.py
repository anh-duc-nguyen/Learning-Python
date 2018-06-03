class Model:
	"""docstring for Model"""
	def __init__(self):
		self.ans = 0
	def setAns(self, ans):
		old = self.ans
		self.ans = ans
		
	def getAns(self):
		return self.ans

	def add(self, first , second):
		ans = first + second
		self.setAns(ans)
	def sub(self, first , second):
		ans = first - second
		self.setAns(ans)
	def mul(self, first , second):
		ans = first * second
		self.setAns(ans)
	def div(self, first , second):
		ans = first / second
		self.setAns(ans)
