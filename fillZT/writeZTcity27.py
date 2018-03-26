##writeZT
# -*- coding: UTF-8 -*-
import time
from pynput.keyboard import Key, Controller
import win32gui
import win32api
import win32con
# from tkinter import *
from controlMouse27home import positionClick,writeCity,restore
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
		# restore()
		clr.print_blue_text("dkdkdkdkdk")
		inputAddress = raw_input("input:")
		with open("ztcity.txt","w+") as f:
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
		with open("ztcity.txt","r") as g:
			writeCity()
			# keyboard.type(("建水").decode("utf-8"))
			with keyboard.pressed(Key.ctrl):
				keyboard.press('a')
				keyboard.release('a')
			print len(g.readlines())
			# print g.readlines()[0].decode("utf-8")
			print g.readlines()[0]
			
			# keyboard.type(g.readlines()[0].decode("utf-8"))
			keyboard.type(str(g.readlines()[0]))
			
			keyboard.press(Key.space)
			time.sleep(0.2)
			keyboard.release(Key.space)
			keyboard.press(Key.tab)
			time.sleep(0.2)
			keyboard.release(Key.tab)
			

		# button = Button(root, text='切换输入', width=25, command=switchInput)
		# button.pack()
		# print (button)
		# restore()
		# time.sleep(0.2)
		# with keyboard.pressed(Key.ctrl):
		# 	# keyboard.pressed(Key.tab)
		# 	keyboard.press(Key.tab)
		# 	time.sleep(0.2)
		# 	keyboard.release(Key.tab)
		r = "ok"
		# root.mainloop()
		# root.update()
def produce(a,d):	
	SWITCH = 0
	a.send(None)
	d.send(None)
	while True:

		SWITCH += 1
		
		r2 = d.send(SWITCH)
		r = a.send(SWITCH)
		
		# time.sleep(1)
		# print (SWITCH)

	
def main():
	a = filled()
	d = writeAddress()
	produce(a,d)
	
if __name__ == '__main__':
	main()


	