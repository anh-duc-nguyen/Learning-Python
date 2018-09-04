
'''
better version of switch. this one is thread safe and 
shorter.
'''


def f(x):
	return {
	'1': one,
	'2': two}.get(x,three)()

def one():
	print('one')
def two():
	print('two')
def three():
	print('three')

def main():
	f('1')

if __name__ == '__main__':
	main()