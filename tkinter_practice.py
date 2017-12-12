from tkinter import *

class MyGUI:
	def __init__(self):
		self.__mainWindow = Tk()
		#self.fram1 = Frame(self.__mainWindow)
		labelText = StringVar()
		self.labelText = 'Enter amount to deposit'
		self.depositLabel = Label(self.__mainWindow, textvariable=labelText)
		self.depositEntry = Entry(self.__mainWindow, width = 10)
		self.depositEntry.bind('<Return>', self.depositCallBack)
		self.depositLabel.pack()
		self.depositEntry.pack()

		mainloop()

	def depositCallBack(self,event):
		labelText.set(txt)
		print(self.labelText)

myGUI = MyGUI()
