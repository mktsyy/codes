##remain
#-*-coding:utf-8-*-

from cutpic import *
 
import ImageEnhance    
import ImageFilter    
import sys    
from pytesser import *  
from recognizenum import *
import time

while True:
	time.sleep(0.2)

	##PLAYER
	cutpic((569,751,746,817),"testnew.jpg")
	img = Image.open("testnew.jpg")
	cutnum(img,(86,1,108,30),'PLAYER-middle.jpg')
	print u"PLAYER-当中是。。。。。"+str(getverify1('PLAYER-middle.jpg'))  #middlecard

	cutnum(img,((140,0,165,31)),'PLAYER-right.jpg')
	print u"PLAYER-右边是。。。。。"+str(getverify1('PLAYER-right.jpg'))  #rightcard

	cutnum(img,((0,30,31,53)),'PLAYER-left.jpg')
	leftpic = Image.open('PLAYER-left.jpg')
	newLP = leftpic.rotate(270)
	newLP.save("PLAYER-left.jpg")
	print u"PLAYER-左边是。。。。。"+str(getverify1('PLAYER-left.jpg'))  #leftcard

	##BANKER

	##导入dos字体变色
	import ctypes

	##dos字体变色
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
	        print print_text
	        self.reset_color()
	    def print_green_text(self, print_text):
	        self.set_cmd_color(FOREGROUND_GREEN | FOREGROUND_INTENSITY)
	        print print_text
	        self.reset_color()
	    def print_blue_text(self, print_text):
	        self.set_cmd_color(FOREGROUND_BLUE | FOREGROUND_INTENSITY)
	        print print_text
	        self.reset_color()
	    def print_red_text_with_blue_bg(self, print_text):
	        self.set_cmd_color(FOREGROUND_RED | FOREGROUND_INTENSITY| BACKGROUND_BLUE | BACKGROUND_INTENSITY)
	        print print_text
	        self.reset_color()  


	clr = Color()
	cutpic((1173,751,1350,817),"BANKER.jpg")
	img = Image.open("BANKER.jpg")
	cutnum(img,(69,1,91,30),'BANKER-middle.jpg')
	clr.print_blue_text(u"BANKER-当中是。。。。。"+str(getverify1('BANKER-middle.jpg')))  #middlecard

	cutnum(img,((112,30,144,54)),'BANKER-right.jpg')
	rightpic = Image.open('BANKER-right.jpg')
	newRP = rightpic.rotate(270)
	newRP.save("BANKER-right.jpg")
	clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

	cutnum(img,((12,1,37,32)),'BANKER-left.jpg')
	clr.print_blue_text(u"BANKER-左边是。。。。。"+str(getverify1('BANKER-left.jpg')))  #leftcard

