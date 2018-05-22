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

from Tkinter import *
import time 
import win32con  
import win32clipboard as w 


root = Tk()
root.wm_attributes('-topmost',1)
var = StringVar()
name = [

u"嗨住深圳01",u"890IOPiop",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳02",u"890IOPiop",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳03",u"890IOPiop",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳04",u"890IOPiop",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳05",u"890IOPiop",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳06",u"123QWEqwe",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳07",u"123qweQ",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳08",u"123qweQ",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳09",u"123qweQ",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住深圳10",u"123qweQ",u"您好，咨询房子请拨打电话：13378414445",
u"嗨住全国01",u"123QWEqwe",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国02",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国03",u"123QWEqwe",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国04",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国05",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国06",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国07",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国08",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国09",u"890IOPiop",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国10",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国11",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国12",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国13",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国14",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国15",u"123qweQ",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住全国16",u"890IOPiop",u"您好，咨询房子请拨打电话：15601708063",
u"嗨住2017",u"890IOPiop",u"您好，咨询房子请拨打电话：13261009316",
u"嗨住2018",u"890IOPiop",u"您好，咨询房子请拨打电话：13261009316",

]

I = 0
def addi():
	global I
	I = I + 1
	# print (name[I])
	setText(name[I])

def deli():
	global I
	I = I - 1
	setText(name[I])

def setText(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard() 

def getText():  
    w.OpenClipboard()  
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)  
    w.CloseClipboard() 

button = Button(root, text='增加',width=25, command=addi)
button.pack()

button = Button(root, text='减少', width=25, command=deli)
button.pack()



Label(root, textvariable = var).pack()

while True:

	var.set(name[I])
	root.update()

