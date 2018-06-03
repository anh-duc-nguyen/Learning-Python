import unittest
from model import *
import random
class ModelTestUnit(unittest.TestCase):
	def setUp(self):
		self.the_model = Model()

	def testSetAndGet(self):
		ans = random.randint(1,100)
		self.the_model.setAns(ans)
		self.assertEqual(self.the_model.getAns(),ans)

	def testSum(self):
		first = random.randint(1,100)
		second = random.randint(1,100)
		ans = first + second
		self.the_model.add(first,second)
		self.assertEqual(self.the_model.getAns(),ans)

	def testSub(self):
		first = random.randint(1,100)
		second = random.randint(1,100)
		ans = first - second
		self.the_model.sub(first,second)
		self.assertEqual(self.the_model.getAns(),ans)

	def testMul(self):
		first = random.randint(1,100)
		second = random.randint(1,100)
		ans = first * second
		self.the_model.mul(first,second)
		self.assertEqual(self.the_model.getAns(),ans)

	def testDiv(self):
		first = random.randint(1,100)
		second = random.randint(1,100)
		ans = first / second
		self.the_model.div(first,second)
		self.assertEqual(self.the_model.getAns(),ans)

if __name__ == '__main__':
	unittest.main()
