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
u"ajk11111",
u"ajk22222",
u"ajk33333",
u"ajk55555",
u"ajk77777",
u"ajk99999",
u"ajk00000",
u"lidan333",
u"lidan222",
u"lidan111",

]

password = [
u"123456a",
u"123456a",
u"123456a",
u"123456a",
u"123456a",
u"123456a",
u"123456a",
u"123456",
u"123456",
u"123456",

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
	sendMessages(u"您好，咨询房子请拨打电话：13024198417")

def addGJPhone():
	# setText(phone[1])
	# fillPhone(phone[1])
	sendMessages(u"您好，咨询房子请拨打电话：13024196747")




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

	def addGJPhone(self,event):
		sendMessages(u"您好，咨询房子可以拨打我的电话13261002623，消息可能无法及时回复，抱歉！")

	def AJKMessage(self,event):
		sendMessages(u"您好，咨询房子请拨打电话：15868422456")


	def addGJMessage(self,event):
		sendMessages(u"您好，咨询房子请拨打电话：15968866951")

	def free(self,event):
		sendMessages(u"我们是免费的租房平台，不收取中介费的")

	def pleaseCall(self,event):
		sendMessages(u"请打客服电话咨询房源信息，我这边查询不了哦！")
		
	def signOut(self,event):
		signOutApp()
	
	def buttonListener1(self,event):
		global I
		I = I + 1
		setText(name[I])
		HZmobilBroker(name[I],password[I])
		##改变标题
		var.set(name[I])

		if name[I] == u"嗨住管家03":
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
		self.button1 = Button(fm2,width=40, text='增加')
		self.button1.pack()
		# Button(fm2, text='This is the Center button').pack(side=LEFT)
		Label(master, textvariable = var).pack(side=BOTTOM)    
		self.button2 = Button(fm2,width=40, text='减少')
		self.button2.pack() 
		self.button6 = Button(fm2,width=40, text='13261002623')
		self.button6.pack()
		# self.button3 = Button(fm2,width=25, text='安居客聊天消息')
		# self.button3.pack()
		  

		# self.button4 = Button(fm2,width=25, text='赶集聊天消息')
		# self.button4.pack()
		self.button7 = Button(fm2,width=40, text='我们是免费的租房平台，不收取中介费的')
		self.button7.pack() 
		self.button8 = Button(fm2, text='请打客服电话咨询房源信息，我这边查询不了哦！')
		self.button8.pack() 
		self.button5 = Button(fm2,width=40, text='退出')
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
		# self.button3.bind("<ButtonRelease-1>",self.AJKMessage)
		# self.button4.bind("<ButtonRelease-1>",self.addGJMessage)
		self.button5.bind("<ButtonRelease-1>",self.signOut)
		self.button6.bind("<ButtonRelease-1>",self.addGJPhone)
		self.button7.bind("<ButtonRelease-1>",self.free)
		self.button8.bind("<ButtonRelease-1>",self.pleaseCall)


root = Tk()
root.title(str(name[I]))
root.wm_attributes('-topmost',1)
var = StringVar()
display = App(root,var)


root.mainloop()
