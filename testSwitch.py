from switch import *

def f1(n):
	while switch(n):
		if case(0):
			print (" It's Zero")
			break
		if case(2,4,6,8):
			print (" it's even" )
			break
		if case(1,3,5,7,9):
			print (" it's odd" )
			break
		print (" one digit only")
		break

def f2(n):
	while switch(n):
		if case(1):
			one()
			break
		if case(2):
			two()
			break
		print("only take 1 or 2 input")
		break

def one():
	print("Function 1")
def two():
	print("Function 2")



def main():
	f1(1)
	f1(0)
	f1(4)
	# f1(2,4,6)
	f1(12)

	f2(1)
	f2(2)
	f2(12)

if __name__ == '__main__':
	main()