##changhelabel
# -*- coding: UTF-8 -*-
# from Tkinter import *
# import globalvarity

# counter = raw_input("input:  ")
# newVar = StringVar()
# def counter_label():
# 	newVar.set(str(globalvarity.COUNTER))
# 	# def count():
# 	# # global counter
# 	# # counter += 1

# 	# 	if globalvarity.A !=globalvarity.COUNTER:
			
# 	# 		globalvarity.A = globalvarity.COUNTER
# 	# 	label.after(1000, count)
# 	# count()
 

# root = Tk()
# root.title("Counting Seconds")

# label = Label(root, fg="green",textvariable = newVar)
# label.pack()
# counter_label()
# # button = Button(root, text='Stop', width=25, command=root.destroy)
# # button.pack()
# root.mainloop()	

from tkinter import *
import time 
import win32con  
import win32clipboard as w 
from fillPic import HZmobilBroker,sendMessages,signOutApp,fillPhone,sendDX


root = Tk()
root.wm_attributes('-topmost',1)
var = StringVar()
name = [
u"嗨住管家03",
u"嗨住管家13",
u"嗨住管家14",
u"嗨住管家15",
u"嗨住管家16",
u"嗨住管家17",
u"嗨住管家18",
u"嗨住管家19",
u"嗨住管家20",
u"嗨住杭州02",
u"嗨住杭州10",
u"嗨住杭州11",
u"嗨住杭州12",
u"嗨住杭州13",
u"嗨住杭州14",
u"嗨住杭州15",
u"嗨住杭州16",
u"嗨住杭州17",
u"嗨住杭州18",
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
u"住017",
u"住018",

]

password = [
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"890WSXwsx",
u"123QAZqaz",
u"123QAZqaz",
u"123QAZqaz",
u"123QAZqaz",
u"123QAZqaz",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",
u"112233Aa",

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
	setText(phone[0])
	fillPhone(phone[0])

def addGJPhone():
	setText(phone[1])
	fillPhone(phone[1])

def AJKMessage():
	sendMessages(u"您好，咨询房子请拨打电话：15868422456")


def addGJMessage():
	sendMessages(u"您好，咨询房子请拨打电话：15968866951")

def signOut():
	signOutApp()


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

button = Button(root, text='增加',width=25, command=addi)
button.pack()

button = Button(root, text='减少', width=25, command=deli)
button.pack()

button = Button(root, text='绑定安居客电话', width=25, command=addAJKPhone)
button.pack()
button = Button(root, text='绑定赶集电话', width=25, command=addGJPhone)
button.pack()

# button = Button(root, text='发送短信', width=25, command=sendDX1)
# button.pack()

button = Button(root, text='安居客聊天消息', width=25, command=AJKMessage)
button.pack()
button = Button(root, text='赶集聊天消息', width=25, command=addGJMessage)
button.pack()

button = Button(root, text='退出', width=25, command=signOut)
button.pack()

Label(root, textvariable = var).pack()

while True:
	root.title(str(name[I]))
	var.set(name[I])
	root.update()

