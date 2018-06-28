#-*-coding:utf-8-*-

from fillPic import HZadmin
from tkinter import *

class App:

	def buttonListener1(self,event):
		HZadmin()

	def __init__(self,master):
		
		self.button1 = Button(width=25,text='操作')
		self.button1.pack()

		##焦点为button1
		self.button1.focus_set()

		self.button1.bind("<ButtonRelease-1>",self.buttonListener1)

root = Tk()
root.title("嗨住后台")
root.wm_attributes('-topmost',1)
display = App(root)
root.mainloop()