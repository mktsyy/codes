# -*- coding: utf-8 -*-

import requests
# import grequests
import json 


##导入界面
from tkinter import *    #注意模块导入方式，否则代码会有差别
import time 
import win32con  
import win32clipboard as w 
from fillPic import HZmobilBroker,sendMessages,signOutApp,fillPhone,sendDX

##Python 下载win32api 模块  终端输入“pip install pypiwin32”

# import win32api, win32gui  
# ct = win32api.GetConsoleTitle()  
# hd = win32gui.FindWindow(0,ct)  
# win32gui.ShowWindow(hd,0)


name = [
u"嗨住管家03",
u"嗨住杭州02",
u"嗨住杭州10",
u"嗨住杭州11",
u"嗨住杭州12",
u"嗨住杭州13",
u"嗨住杭州14",
u"嗨住杭州15",
u"嗨住杭州17",
u"嗨住杭州19",
u"嗨住杭州20",
u"嗨住杭州21",
u"嗨住杭州22",
u"嗨住杭州23",
u"嗨住杭州24",
u"嗨住杭州25",
u"嗨住杭州26",
u"嗨住杭州27",
u"嗨住杭州28",
u"嗨住杭州29",
u"住001",
u"住002",
u"住003",
u"住004",
u"住005",
u"住006",
u"住007",
u"住008",
u"住009",
u"住010",
u"住011",
u"住012",
u"住013",
u"住014",
u"住015",
u"住016",



]

password = [
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"890WSXwsx",
"123QAZqaz",
"123QAZqaz",
"123QAZqaz",
"123QAZqaz",
"123QAZqaz",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",
"112233Aa",



]

phone =[
"15868422456",
"15968866951"
]

I = -1
def addi():
	# print (name[I])
	global I
	I = I + 1
	setText(name[I])
	HZmobilBroker(name[I],password[I])
	

def deli():
	global I
	I = I - 1
	setText(name[I])
	HZmobilBroker(name[I],password[I])

def addAJKPhone():
	# setText(phone[0])
	# fillPhone(phone[0])
	sendMessages(u"")

def addGJPhone():
	# setText(phone[1])
	# fillPhone(phone[1])
	sendMessages(u"")




def setText(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard() 

def getText():  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)  
    w.CloseClipboard() 

def sendDX1():
	sendDX()


class App:

	def addHZajkPhone(self,event):
		sendMessages(u"您好，咨询房子可以拨打我的电话15868422456，消息可能无法及时回复，抱歉！")

	def WHGJMessage(self,event):
		sendMessages(u"")


	def addHZMessage(self,event):
		sendMessages(u"您好，咨询房子可以拨打我的电话15968866951，消息可能无法及时回复，抱歉！")

	def addWHajkPhone(self,event):
		sendMessages(u"")

	def mfzf(self,event):
		sendMessages(u"我们是免费的租房平台，不收取中介费的。")

	def signOut(self,event):
		signOutApp()
	
	def buttonListener1(self,event):
		global I
		I = I + 1
		setText(name[I])
		HZmobilBroker(name[I],password[I])
		##改变标题
		var.set(name[I])

		if name[I] == u"":
			self.button6.state= "normal"
		else:
			self.button6.state = "disabled"
		
		

	def buttonListener2(self,event):
		global I
		I = I - 1
		setText(name[I])
		HZmobilBroker(name[I],password[I])
		##改变标题
		var.set(name[I])
	
	def __init__(self, master,var):
		#使用Frame增加一层容器
		

		##初始化框体大小
		fm2 = Frame(master,width = 250,height=200)

		##加入事件绑定
		self.button1 = Button(fm2,width=25, text='增加')
		self.button1.pack()
		# Button(fm2, text='This is the Center button').pack(side=LEFT)
		Label(master, textvariable = var).pack(side=BOTTOM)    
		self.button2 = Button(fm2,width=25, text='减少')
		self.button2.pack() 
		self.button6 = Button(fm2,width=25, text='杭州安居客聊天消息')
		self.button6.pack()

		# self.button7 = Button(fm2,width=25, text='武汉安居客聊天消息')
		# self.button7.pack()

		# self.button3 = Button(fm2,width=25, text='武汉赶集聊天消息')
		# self.button3.pack()
		  

		self.button4 = Button(fm2,width=25, text='杭州赶集聊天消息')
		self.button4.pack() 

		self.button8 = Button(fm2,width=25, text='免费租房')
		self.button8.pack() 

		self.button5 = Button(fm2,width=25, text='退出')
		self.button5.pack()   

		##使大小生效
		###http://effbot.org/tkinterbook/button.htm这里官方解释为don't shrink
		# fm2.pack_propagate(0)
		##参数详见https://www.cnblogs.com/muziyunxuan/p/8268179.html
		fm2.pack()


		##焦点为button1
		self.button1.focus_set()



		self.button1.bind("<ButtonRelease-1>",self.buttonListener1)
		self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
		# self.button3.bind("<ButtonRelease-1>",self.WHGJMessage)
		self.button4.bind("<ButtonRelease-1>",self.addHZMessage)
		self.button5.bind("<ButtonRelease-1>",self.signOut)
		self.button6.bind("<ButtonRelease-1>",self.addHZajkPhone)
		# self.button7.bind("<ButtonRelease-1>",self.addWHajkPhone)
		self.button8.bind("<ButtonRelease-1>",self.mfzf)


root = Tk()
# root.title(str(name[I]))
root.wm_attributes('-topmost',1)
var = StringVar()
display = App(root,var)


root.mainloop()
