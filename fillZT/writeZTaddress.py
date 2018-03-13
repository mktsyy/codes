##writeZT

# -*- coding: UTF-8 -*-
import time
from pynput.keyboard import Key, Controller
import win32gui
import win32api
import win32con
from tkinter import *
from controlMouse import positionClick,restore
import ctypes


STD_INPUT_HANDLE = -10
STD_OUTPUT_HANDLE= -11
STD_ERROR_HANDLE = -12
FOREGROUND_BLACK = 0x0
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED = 0x04 # text color contains red.
FOREGROUND_INTENSITY = 0x08 # text color is intensified.
BACKGROUND_BLUE = 0x10 # background color contains blue.
BACKGROUND_GREEN= 0x20 # background color contains green.
BACKGROUND_RED = 0x40 # background color contains red.
BACKGROUND_INTENSITY = 0x80 # background color is intensified.
class Color:
    ''' See http://msdn.microsoft.com/library/default.asp?url=/library/en-us/winprog/winprog/windows_api_reference.asp
    for information on Windows APIs. - www.jb51.net'''
    std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    def set_cmd_color(self, color, handle=std_out_handle):
        """(color) -> bit
        Example: set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        """
        bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
        return bool
    def reset_color(self):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_GREEN | FOREGROUND_BLUE)
    def print_red_text(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY)
        print (print_text)
        self.reset_color()
    def print_green_text(self, print_text):
        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
        print (print_text)
        self.reset_color()
    def print_blue_text(self, print_text):
        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
        print (print_text)
        self.reset_color()
    def print_red_text_with_blue_bg(self, print_text):
        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)
        print (print_text)
        self.reset_color()  

keyboard = Controller()
# wdname1=u"zt.txt - 记事本"
# w1hd=win32gui.FindWindow(0,wdname1)
# w2hd=win32gui.FindWindowEx(w1hd,None,None,None)
# win32gui.SetForegroundWindow(w2hd)
clr = Color()

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
		clr.print_red_text("地址地址地址") 
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
			# with keyboard.pressed(Key.ctrl):
			# 	keyboard.press('a')
			# 	keyboard.release('a')
			keyboard.type(g.readlines()[0])

		# button = Button(root, text='切换输入', width=25, command=switchInput)
		# button.pack()
		# print (button延长中路500号		# restore()
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


	