#-*-coding:utf-8-*-


from tkinter import *
from tkinter import ttk
import os
import time
from fillPic import cityMouse,counterNum,selectCancel,firstSendCancle,dueCancle

class App:

	def buttonListener1(self,event):
		# HZadmin()
		##打印绑定的账号
		print(self.button1.get())
		cityMouse(self.button1.get())


	def buttonListener2(self,event):
		counterNum()

	def buttonListener3(self,event):
		var = self.e.get()
		# var = 0
		selectCancel(var)


	def buttonListener4(self,event):
		firstSendCancle()

	def buttonListener5(self,event):
		dueCancle()
		


	def __init__(self,master):

		
		
		##用框架，grid方法来划分
		frame1 = Frame(master)
		frame1.pack()  #看下面的解释（包管理器）
		self.label = Label(frame1,text = "选择：")
		self.label.grid(row = 1, column = 0)

		##不再需要翻页方法
		# self.button1 = Button(frame1,width=15,text='操作')
		# self.button1.grid(row = 1, column = 2)

		##重新定义为选择框，选择发布账号
		number = StringVar()
		self.button1 = ttk.Combobox(frame1,width=38,text=number)
		self.button1['values'] = ("http://vip.58ganji.com/zf58/kcfy58/W0QQpZ6",  \
								"http://vip.58ganji.com/zf58/yxtg58/W0QQpZ36", \
								"http://vip.58ganji.com/zf58/yxtg58/W0QQpZ20",
								"http://vip.58ganji.com/zf58/yxtg58/W0QQpZ10",
								"http://vip.58ganji.com/zf58/yxtg58/W0QQpZ30",
								"http://vip.58ganji.com/zf58/cxfy58/W0QQpZ3",
								"http://vip.58ganji.com/zf58/kcfy58  ",
								
								   ) 
		self.button1.grid(row = 1, column = 1, columnspan=3)

		self.label = Label(frame1,text = "取消数量：")
		self.label.grid(row = 2, column = 0)
		##加入输入框准备后端获取链接，进行改造
		self.e = Entry(frame1,width=40)
		self.e.grid(row = 2, column = 1, columnspan=3)

		self.button2 = Button(frame1,text='统计本页优先推送数量')
		self.button2.grid(row = 3, column = 0)
		self.button3 = Button(frame1,text='勾选取消推送')
		self.button3.grid(row = 3, column = 1)
		##获取输入框内容按钮
		self.button4 = Button(frame1,text='批量取消')
		self.button4.grid(row = 3, column = 2)

		##取消红色推送快到期房源
		self.button5 = Button(frame1,text='批量取消推送红色房源')
		self.button5.grid(row = 3, column = 3)

		##焦点为button1
		self.button1.focus_set()

		self.button1.bind("<<ComboboxSelected>>",self.buttonListener1)
		self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
		self.button3.bind("<ButtonRelease-1>",self.buttonListener3)
		self.button4.bind("<ButtonRelease-1>",self.buttonListener4)
		self.button5.bind("<ButtonRelease-1>",self.buttonListener5)

root = Tk()
root.title("58同城")
root.wm_attributes('-topmost',1)
display = App(root)
root.mainloop()