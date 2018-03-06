# -*- coding: UTF-8 -*-

from tkinter import *
import win32gui
import win32con



# top = Tk()
# top.title ("Casino Recognize")
# ##窗口置顶
# top.wm_attributes('-topmost',1)
# # 进入消息循环
# kk = (2,3,4,5,6,7,8,9,10,222,222,222,8888)
# allCard ='''
# 2:%d \n
# 3:%d \n
# 4:%d \n
# 5:%d \n
# 6:%d \n
# 7:%d \n
# 8:%d \n
# 9:%d \n
# 10:%d \n
# J:%d \n
# Q:%d \n
# K:%d \n
# total:%d \n
# ''' % kk
# Label(top,text=allCard,font=50,).pack(side="left")

# ##用找焦点的方法失败了，还是网上查到了另外一个方法
# # wdname1=u"Casino Recognize"
# # w1hd=win32gui.FindWindow(0,wdname1)
# # w2hd=win32gui.FindWindowEx(w1hd,None,None,None)
# # # print (type(window.handle))
# # win32gui.SetForegroundWindow(w2hd)
# # HWND = win32gui.GetForegroundWindow()
# # print (type(HWND))
# # win32gui.SetWindowPos(HWND,win32con.HWND_TOPMOST,0,0,0,0, win32con.SWP_NOMOVE | win32con.SWP_NOACTIVATE| win32con.SWP_NOOWNERZORDER|win32con.SWP_SHOWWINDOW)

##mainloop是属于block的，无法介入，要不想阻塞，用update或update_idletasks，update高于update_idletasks
# top.mainloop()


# from tkinter import *
# import time

# root = Tk()
# var = StringVar()
# var.set('hello')

# l = Label(root, textvariable = var)
# l.pack()

##输入框
# t = Entry(root, textvariable = var)
# t.pack()

# time.sleep(2)
# var.set('kill')
# root.mainloop() # the window is now displayed



from tkinter import *
from time import sleep

root = Tk()
##tk中独有的变量
var = StringVar()

root.title ("Casino Recognize")
##窗口置顶
root.wm_attributes('-topmost',1)
##label标签设置文本变量
Label(root, textvariable = var).pack()


##仅6次展示
# for i in range(6):
#     sleep(1) # Need this to slow the changes down
#     var.set('goodbye' if i%2 else 'hello')
#     # root.update_idletasks()
#     root.update()
##循环展示
i = 1

while True:
	var.set('goodbye' if i%2 else 'hello')
	root.update()
	i +=1
	sleep(1)

##测试使用update_idletasks方法还是update方法，更详细的解释见https://stackoverflow.com/questions/29158220/tkinter-understanding-mainloop
# i = 2
# var.set('goodbye' if i%2 else 'hello')
# root.update()

# sleep(4)


# i = 1
# var.set('goodbye' if i%2 else 'hello')
# # root.update_idletasks()
# root.update()
# sleep(4)
# i = 2
# var.set('goodbye' if i%2 else 'hello')
# # root.update_idletasks()
# root.update()

# sleep(4)