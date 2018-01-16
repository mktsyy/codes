##Coroutine
#- * -coding: utf - 8 - * -

from getPicture import *
 
import ImageEnhance    
import ImageFilter    
import sys    
from pytesser import *  
from recognizenum import *
import time
from PIL import Image,ImageGrab
import when
import os
from multiprocessing import Process,Manager,Lock
import ctypes

# from ipdb import set_trace

# set_trace()

ifcolor = []
for i in xrange(210,256):
	for n in xrange(210,256):
		for g in xrange(210,256):
			ifcolor.append((i,n,g))

img = Image.open("testnew.jpg")

imgBANKER = Image.open("BANKER.jpg")

def ScreenShot():
	im = ImageGrab.grab() 
	im.save(os.getcwd()+"/screenshot.png")#保存图片 

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
    def intCardNum(self,strnum):
    	if strnum not in "12345678910JQKA":
			pass
    	else:
    		if strnum in "10JQK":
    			tempnum = 0
    		elif strnum in "A":
    			tempnum = 1
    		else:
    			tempnum = int(strnum)
    	return tempnum

clr = Color()

def consumer():
	r = ''
	while True:
		n = yield r
		print n
		if not n:
			return

		print('[CONSUMER] Consuming %s...' % n)

		# from IPython import embed
		# embed()
		img = Image.open("testnew.jpg")

		imgBANKER = Image.open("BANKER.jpg")

		cutnum(img,(86,1,111,30),'PLAYER-middle.jpg')
		# from IPython import embed
		# embed()
		print u"PLAYER-当中是。。。。。"+str(getverify1('PLAYER-middle.jpg'))  #middlecard
		# from IPython import embed
		# embed()

		cutnum(img,((138,1,167,31)),'PLAYER-right.jpg')
		print u"PLAYER-右边是。。。。。"+str(getverify1('PLAYER-right.jpg'))  #rightcard
		
		cutnum(imgBANKER,(69,1,92,32),'BANKER-middle.jpg')
		clr.print_blue_text(u"BANKER-当中是。。。。。"+str(getverify1('BANKER-middle.jpg')))  #middlecard
		
		cutnum(imgBANKER,((12,1,39,32)),'BANKER-left.jpg')
		clr.print_blue_text(u"BANKER-左边是。。。。。"+str(getverify1('BANKER-left.jpg')))  #leftcard

		r = '200 OK'

def produce(c):
	c.send(None)
	n = 0
	while True:

		
		n = n + 1
		time.sleep(0.2)
		ScreenShot()
		time.sleep(0.2)
		cutpic((569,751,746,817),"testnew.jpg")
		cutpic((1173,751,1350,817),"BANKER.jpg")

		img = Image.open("testnew.jpg")

		imgBANKER = Image.open("BANKER.jpg")
		
		print('[PRODUCER] Producing %s...' % n)

		# from IPython import embed
		# embed()

		if img.getpixel((79,16))  in ifcolor  and imgBANKER.getpixel((62,26)) in ifcolor  \
		and img.getpixel((130,3)) in ifcolor and imgBANKER.getpixel((7,26)) in ifcolor \
		and imgBANKER.getpixel((2,3)) in ifcolor and imgBANKER.getpixel((103,3)) in ifcolor:
			r = c.send(n)
			print ('[PRODUCER] Consumer return: %s' % r)
			


		# r = c.send(n)
		# print('[PRODUCER] Consumer return: %s' % r)

		
	c.close()


def main():
	c = consumer()
	produce(c)
	
if __name__ == '__main__':
	main()