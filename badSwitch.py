'''
DO NOT USE:: This is not thread safe
A switch class for creating switch in Python
@author: anh nguyen
@version: 1.1
'''

class switch(object):
	value = None
	def __new__(class_, value):
		class_.value = value
		return True
def case(*args):
	return any(( arg== switch.value for arg in args))


# Usage:
# def main(n):
# 	while switch(n):
# 		if case(0):
# 			print (" It's Zero")
# 			break
# 		if case(2,4,6,8):
# 			print (" it's even" )
# 			break
# 		if case(1,3,5,7,9):
# 			print (" it's odd" )
# 			break
# 		print (" one digit only")
# 		break
# if __name__ == '__main__':
# 	main(1)