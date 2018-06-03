from model import *
from view import *

class Control:
	def __init__(self,view,model):
		self.theView = view
		self.theModel = model
		self.theView.addButton.bind("<Button-1>",self.pressAdd)
		self.theView.subButton.bind("<Button-1>",self.pressSub)
		self.theView.mulButton.bind("<Button-1>",self.pressMul)
		self.theView.divButton.bind("<Button-1>",self.pressDiv)
		self.theView.clrButton.bind("<Button-1>",self.pressClr)
				

	def pressAdd(self,event):
		first = self.theView.getFirst()
		second = self.theView.getSecond()
		self.theModel.add(first,second)
		ans = self.theModel.getAns()
		self.theView.setAns(ans)

	def pressSub(self,event):
		first = self.theView.getFirst()
		second = self.theView.getSecond()
		self.theModel.sub(first,second)
		ans = self.theModel.getAns()
		self.theView.setAns(ans)

	def pressMul(self,event):
		first = self.theView.getFirst()
		second = self.theView.getSecond()
		self.theModel.mul(first,second)
		ans = self.theModel.getAns()
		self.theView.setAns(ans)

	def pressDiv(self,event):
		first = self.theView.getFirst()
		second = self.theView.getSecond()
		self.theModel.div(first,second)
		ans = self.theModel.getAns()
		self.theView.setAns(ans)

	def pressClr(self,event):
		self.theView.setAns(0)

if __name__ == '__main__':
	theView = View()
	theModel = Model()
	theControl = Control(theView,theModel)
	theView.build()
		