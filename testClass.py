class superClass:
	""" a Super class"""
	def __init__(self, name):
		self.name = name
	
	def toString(self):
		return self.name

class testClass(superClass):
	"""a child class inheritance of Super class"""
	def __init__(self, name):
		superClass.__init__(self,name)

def test():
	'''
	test program for class inheritance
	'''
	a = superClass("alex")
	b = testClass("bob")
	print ( a.toString() )
	print ( b.toString() )

if __name__ == '__main__':
	test()
		
		