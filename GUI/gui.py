# -*- coding: UTF-8 -*-

from tkinter import *
top = Tk()
top.title ("Casino Recognize")
# 进入消息循环
allCard ='''
2:%d \n
3:%d \n
4:%d \n
5:%d \n
6:%d \n
7:%d \n
8:%d \n
9:%d \n
10:%d \n
J:%d \n
Q:%d \n
K:%d \n
total:%d \n
''' % (2,3,4,5,6,7,8,9,10,222,222,222,88888)
Label(top,text=allCard,font=50,).pack(side="left")
top.mainloop()