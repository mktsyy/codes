##writeZT

# -*- coding: UTF-8 -*-
import time
from pynput.keyboard import Key, Controller
import win32gui
import win32api
import win32con
from tkinter import *
from controlMouse import positionClick,restore

keyboard = Controller()
# wdname1=u"zt.txt - 记事本"
# w1hd=win32gui.FindWindow(0,wdname1)
# w2hd=win32gui.FindWindowEx(w1hd,None,None,None)
# win32gui.SetForegroundWindow(w2hd)


def switchInput():
	SWITCH = 0
	root.destroy()

def writeAddress():
	r = ""
	while True:
		n = yield r
		# print n
		if not n:
			return
		inputAddress = input("输入地址：")
		with open("zt.txt","w+",encoding="utf-8") as f:
			f.write(inputAddress)
		r = "gogogo"
	

def filled():
	r = ""
	while True:
		n = yield r
		# print n
		if not n:
			return
		##python3的写法，python2的话不用加encoding="utf-8"
		with open("zt.txt","r",encoding="utf-8") as g:
			positionClick()
			with keyboard.pressed(Key.ctrl):
				keyboard.press('a')
				keyboard.release('a')
			keyboard.type(g.readlines()[0])

		# button = Button(root, text='切换输入', width=25, command=switchInput)
		# button.pack()
		# print (button)
		restore()
		r = "ok"
		# root.mainloop()
		# root.update()
def produce(a,d):	
	SWITCH = 0
	a.send(None)
	d.send(None)
	while True:

		SWITCH += 1
		
		r = a.send(SWITCH)
		
		r2 = d.send(SWITCH)
		# time.sleep(1)
		# print (SWITCH)

	
def main():
	a = filled()
	d = writeAddress()
	produce(a,d)
	
if __name__ == '__main__':
	main()


	