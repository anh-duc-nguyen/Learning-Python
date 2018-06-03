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

		self.addButton = Button(self.frame, text="*")
		# self.addButton.bind(self.pressAdd)
		self.addButton.pack(side=LEFT, fill = X)

		self.subButton = Button(self.frame, text="-")
		# self.subButton.bind(self.pressSub)
		self.subButton.pack(side=LEFT, fill = X)
		self.mulButton = Button(self.frame, text="*")
		# self.mulButton.bind(self.pressMul)
		self.mulButton.pack(side=LEFT, fill = X)
		self.divButton = Button(self.frame, text="/")
		# self.divButton.bind(self.pressDiv)
		self.divButton.pack(side=LEFT, fill = X)
		self.clrButton = Button(self.frame, text="CLEAR")
		self.clrButton.pack(side=LEFT, fill = X)

	# def getFirst(self):
	# 	print self.ansEntry.get()

	# def pressAdd(self):
	# 	pass
	# def pressSub(self):
	# 	pass
	# def pressMul(self):
	# 	pass
	# def pressDiv(self):
	# 	pass

	def getFirst(self):
		return int (self.firstEntry.get())

	def getSecond(self):
		return int (self.secondEntry.get())

	def setAns(self,ans):
		self.ansEntry.delete(0,END)
		self.ansEntry.insert(0,ans)
		
	def build(self):
		self.frame.pack()
		self.root.mainloop()

if __name__ == '__main__':
	theView = View()
	theView.build()
