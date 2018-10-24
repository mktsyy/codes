# -*- coding: utf-8 -*-

import requests
# import grequests
import json 


##导入界面
from tkinter import *    #注意模块导入方式，否则代码会有差别
import tkinter.messagebox
import time 
import win32con  
import win32clipboard as w 
from fillPic import HZmobilBroker,sendMessages,signOutApp,fillPhone,sendDX,HZmobilBrokerMI,signOutAppMI,sendMessagesMI,getPos
from saveI import saveIMI,saveI
import os,sys
##Python 下载win32api 模块  终端输入“pip install pypiwin32”

# import win32api, win32gui  
# ct = win32api.GetConsoleTitle()  
# hd = win32gui.FindWindow(0,ct)  
# win32gui.ShowWindow(hd,0)


name = [
# u"南京嗨住租房01",
# u"南京嗨住租房02",
# u"南京嗨住租房03",
# u"南京嗨住租房04",
# u"南京嗨住租房05",
# u"南京嗨住租房06",
# u"南京嗨住租房07",
# u"南京嗨住租房08",
# u"南京嗨住租房09",
# u"南京嗨住租房10",
# u"南京嗨住租房11",
# u"南京嗨住租房12",
u"南京嗨住租房13",
# u"南京嗨住租房14",
# u"南京嗨住租房15",
# u"南京嗨住租房16",
# u"南京嗨住租房17",
# u"南京嗨住租房18",
# u"南京嗨住租房19",
# u"南京嗨住租房20",
u"嗨住21",
u"嗨住22",
u"嗨住23",
u"嗨住24",
u"嗨住25",
u"南京嗨住02",
u"南京嗨住03",
u"南京嗨住04",
u"南京嗨住05",
u"南京嗨住15",
u"南京嗨住16",
u"南京嗨住17",
u"南京嗨住18",
u"南京嗨住19",
u"南京嗨住20",
# u"武汉嗨住租房01",
# u"武汉嗨住租房02",
# u"武汉嗨住01",
# u"武汉嗨住02",
# u"武汉嗨住03",
# u"武汉嗨住04",
# u"武汉嗨住05",
# u"武汉嗨住06",


]

password = [
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
"123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
# "123456",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
"112233",
# "a123456",
# "a123456",
# "a123456",
# "a123456",
# "a123456",
# "a123456",
# "a123456",
# "a123456",


]

phone =[
"15868422456",
"15968866951"
]

I =-1
def addi():
	# print (name[I])
	global I
	I = I + 1
	setText(name[I])
	# HZmobilBroker(name[I],password[I])
	HZmobilBrokerMI(name[I],password[I])

	

def deli():
	global I
	I = I - 1
	setText(name[I])
	# HZmobilBroker(name[I],password[I])
	HZmobilBrokerMI(name[I],password[I])

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

	def addNJajkPhone(self,event):
		setText(u"您好，咨询房子可以拨打我的电话17388078735，消息可能无法及时回复，抱歉！")
		sendMessages(u"您好，咨询房子可以拨打我的电话17388078735，消息可能无法及时回复，抱歉！")

	def WHGJMessage(self,event):
		setText(u"您好，咨询房子可以拨打我的电话13024114908，消息可能无法及时回复，抱歉！")
		sendMessages(u"您好，咨询房子可以拨打我的电话13024114908，消息可能无法及时回复，抱歉！")


	def addNJGJMessage(self,event):
		setText(u"您好，咨询房子可以拨打我的电话17327798350，消息可能无法及时回复，抱歉！")
		sendMessages(u"您好，咨询房子可以拨打我的电话17327798350，消息可能无法及时回复，抱歉！")

	def addWHajkPhone(self,event):
		setText(u"您好，咨询房子可以拨打我的电话13517269813，消息可能无法及时回复，抱歉！")
		sendMessages(u"您好，咨询房子可以拨打我的电话13517269813，消息可能无法及时回复，抱歉！")

	def mfzf(self,event):
		setText(u"我们是免费的租房平台，不收取中介费的。")
		sendMessages(u"我们是免费的租房平台，不收取中介费的。")

	def signOut(self,event):
		global I
		if I == len(name) - 1:
			I = -1
			saveIMI(I)
			
			##弹出账号循环提示消息
			tkinter.messagebox.showinfo(message="账号将重新循环！")

		signOutAppMI()

	
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

	def restartApp(self,event):
		##重启程序
		python = sys.executable
		os.execl(python, python, * sys.argv)

	def setPos(self,event):
		##更改程序位置
		getPos()

		##记住I位置
		global I
		saveIMI(I)
		
		##重启程序
		python = sys.executable
		os.execl(python, python, * sys.argv)

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
		self.button6 = Button(fm2,width=25, text='南京安居客聊天消息')
		self.button6.pack()

		self.button4 = Button(fm2,width=25, text='南京赶集聊天消息')
		self.button4.pack() 

		# self.button7 = Button(fm2,width=25, text='武汉安居客聊天消息')
		# self.button7.pack()

		# self.button3 = Button(fm2,width=25, text='武汉赶集聊天消息')
		# self.button3.pack()
		  


		self.button8 = Button(fm2,width=25, text='免费租房')
		self.button8.pack() 

		# self.button9 = Button(fm2,width=25, text='重启程序')
		# self.button9.pack() 

		self.button10 = Button(fm2,width=25, text='定位设置')
		self.button10.pack() 

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
		self.button4.bind("<ButtonRelease-1>",self.addNJGJMessage)
		self.button5.bind("<ButtonRelease-1>",self.signOut)
		self.button6.bind("<ButtonRelease-1>",self.addNJajkPhone)
		# self.button7.bind("<ButtonRelease-1>",self.addWHajkPhone)
		self.button8.bind("<ButtonRelease-1>",self.mfzf)
		# self.button9.bind("<ButtonRelease-1>",self.restartApp)
		self.button10.bind("<ButtonRelease-1>",self.setPos)


root = Tk()
# root.title(str(name[I]))
root.wm_attributes('-topmost',1)

##界面出现位置（宽*高+离左边缘距离+离顶端距离）
##见https://blog.csdn.net/Mrliangqixiong/article/details/80934842
root.geometry("200x300+1300+500")

var = StringVar()
display = App(root,var)


root.mainloop()
