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
from controlMouse import position,exita,positionMI,exitaMI,posMes


root = Tk()
root.wm_attributes('-topmost',1)
var = StringVar()
name = [

u"嗨住深圳01",u"890IOPiop",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳02",u"890IOPiop",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳03",u"890IOPiop",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳04",u"890IOPiop",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳05",u"890IOPiop",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳06",u"123QWEqwe",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳07",u"123qweQ",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳08",u"123qweQ",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳09",u"123qweQ",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住深圳10",u"123qweQ",u"您好，咨询房子可以拨打我的电话17701674748，消息可能无法及时回复，抱歉！",
u"嗨住全国01",u"123QWEqwe",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国02",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国03",u"123QWEqwe",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国04",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国05",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国06",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国07",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国08",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国09",u"890IOPiop",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国10",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国11",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国12",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国13",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国14",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国15",u"123qweQ",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住全国16",u"890IOPiop",u"您好，咨询房子可以拨打我的电话15601708063，消息可能无法及时回复，抱歉！",
u"嗨住2017",u"890IOPiop",u"您好，咨询房子可以拨打我的电话13261009316，消息可能无法及时回复，抱歉！",
u"嗨住2018",u"890IOPiop",u"您好，咨询房子可以拨打我的电话13261009316，消息可能无法及时回复，抱歉！",
u"上海高度公司",u"Abc1234",u"您好，咨询房子可以拨打我的电话13024183940，消息可能无法及时回复，抱歉！",
u"高度公寓2018",u"a12345.",u"您好，咨询房子可以拨打我的电话18664756582，消息可能无法及时回复，抱歉！",

]

I = -3
def addi():
	global I
	I = I + 3
	# print (name[I])
	position(name[I],name[I+1])
	setText(name[I+2])
	

def deli():
	global I
	I = I - 3
	position(name[I],name[I+1])
	setText(name[I+2])

def exitApp():
	exita()

def exitAppMI():
	exitaMI()


def setText(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard() 

def getText():  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)  
    w.CloseClipboard() 

def free():
	posMes(u"我们是免费的租房平台，不收取中介费的")
	global I
	setText(name[I+2])


def pleaseCall():
	posMes(u"请打客服电话咨询房源信息，我这边查询不了哦！")
	global I
	setText(name[I+2])

button = Button(root, text='增加',width=25, command=addi)
button.pack()

button = Button(root, text='减少', width=25, command=deli)
button.pack()

button = Button(root, text='退出', width=25, command=exitApp)
button.pack()

# button = Button(root, text='退出', width=25, command=exitAppMI)
# button.pack()

button = Button(root, text='免费的租房平台', width=25, command=free)
button.pack()

button = Button(root, text='请打客服电话', width=25, command=pleaseCall)
button.pack()


# button = Button(root, text='17701674748', width=25, command=setText(u"您好，咨询房子请拨打电话：13378414445"))
# button.pack()

# button = Button(root, text='13378414445', width=25, command=setText(u"您好，咨询房子请拨打电话：15601708063"))
# button.pack()


Label(root, textvariable = var).pack()

while True:
	var.set(name[I])
	root.update()

