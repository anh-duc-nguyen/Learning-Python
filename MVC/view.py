from Tkinter import *


class View:
	def __init__(self):
		self.first = 0
		self.second = 0
		self.ans = 0
		
		self.root = Tk()
		self.frame = Frame(self.root)
		
		self.firstEntry = Entry(self.root)
		self.firstEntry.pack(side=TOP)

		self.secondEntry = Entry(self.root)
		self.secondEntry.pack(side=TOP)

		self.ansEntry = Entry (self.root)
		self.ansEntry.pack(side=BOTTOM)
		
		Label(self.frame, text = "simple Calculator").pack()

		addButton = Button(self.frame, text="add")
		addButton.bind(self.pressSum)
		addButton.pack(side=LEFT, fill = Y)

		subButton = Button(self.frame, text="sub")
		subButton.bind(self.pressSub)
		subButton.pack(side=LEFT, fill = Y)
		mulButton = Button(self.frame, text="mul")
		mulButton.bind(self.pressMul)
		mulButton.pack(side=LEFT, fill = Y)
		divButton = Button(self.frame, text="div")
		divButton.bind(self.pressDiv)
		divButton.pack(side=LEFT, fill = Y)


	
	def pressSum(self):
		pass
	def pressSub(self):
		pass
	def pressMul(self):
		pass
	def pressDiv(self):
		pass

	def build(self):
		self.frame.pack()
		self.root.mainloop()

if __name__ == '__main__':
	theView = View()
	theView.build()