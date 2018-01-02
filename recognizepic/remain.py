##remain
#-*-coding:utf-8-*-

from cutpic import *
 
import ImageEnhance    
import ImageFilter    
import sys    
from pytesser import *  
from recognizenum import *
import time


# ifcolor = [(233, 241, 243),(237, 238, 240),(238, 240, 239),(235, 237, 236),(236, 238, 237),
#           (237, 238, 233),(242, 239, 232),(248, 233, 228),(235, 239, 238),(238, 238, 238),
#           (233, 239, 239),(237, 237, 237),(241, 236, 232),(255, 231, 237),(235, 241, 237),
#           (234, 240, 238),(237, 238, 243),(251, 230, 235),(231, 241, 242),
#           (52, 111, 119),(243, 238, 234),(231, 243, 239),(238, 239, 243),(227, 244, 238),
#           (232, 241, 246),(236, 239, 244),(231, 243, 239),(245, 235, 233),(250, 229, 234),
#           (231, 243, 241), (221, 244, 250), (235, 240, 244), (231, 243, 241), (239, 238, 243),
#           (242, 237, 233), (243, 236, 226),(243, 238, 232),(234, 239, 242),(230, 241, 247),
#           (64, 100, 90), (237, 239, 238), (240, 237, 232),(236, 240, 241),
#           (245, 234, 228), (245, 237, 234), (243, 236, 228),(248, 233, 226),(232, 241, 240),
#           (247, 232, 225),(239, 236, 231),(239, 237, 240),(252, 234, 234),(243, 238, 219),
# 		(231, 231, 229),(236, 239, 230),(241, 226, 229),(252, 238, 235),
#           (238, 242, 241), (235, 239, 240), (246, 233, 225), (240, 237, 232),
#           (247, 234, 228), (243, 240, 221),(240, 237, 244),(247, 232, 235),

#           (235, 240, 243), (238, 239, 244), (243, 234, 227), (247, 236, 234),
#           (245, 245, 243), (235, 241, 241), (238, 237, 242), (238, 238, 240),
#            ]

ifcolor = []
for i in xrange(210,255):
	for n in xrange(210,255):
		for g in xrange(210,255):
			ifcolor.append((i,n,g))



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


while True:
	time.sleep(2)

	##PLAYER

	cutpic((569,751,746,817),"testnew.jpg")
	cutpic((1173,751,1350,817),"BANKER.jpg")

	clr = Color()

	img = Image.open("testnew.jpg")

	imgBANKER = Image.open("BANKER.jpg")
	
	# print img.getpixel((23,23))
	if img.getpixel((23,23)) in ifcolor:
		cutnum(img,((0,30,34,53)),'PLAYER-left.jpg')
		leftpic = Image.open('PLAYER-left.jpg')
		newLP = leftpic.rotate(270)
		newLP.save("PLAYER-left.jpg")
		print u"PLAYER-左边是。。。。。"+str(getverify1('PLAYER-left.jpg'))  #leftcard

	# print img.getpixel((137,26))
	if imgBANKER.getpixel((137,26)) in ifcolor:
		cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		rightpic = Image.open('BANKER-right.jpg')
		newRP = rightpic.rotate(270)
		newRP.save("BANKER-right.jpg")
		clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard
		time.sleep(3)
		continue

	# print img.getpixel((79,16))
	if img.getpixel((79,16))  in ifcolor  and imgBANKER.getpixel((62,26)) in ifcolor and img.getpixel((134,16)) in ifcolor and imgBANKER.getpixel((7,26)) in ifcolor:
		cutnum(img,(86,1,111,30),'PLAYER-middle.jpg')
		print u"PLAYER-当中是。。。。。"+str(getverify1('PLAYER-middle.jpg'))  #middlecard

		cutnum(img,((138,1,167,31)),'PLAYER-right.jpg')
		print u"PLAYER-右边是。。。。。"+str(getverify1('PLAYER-right.jpg'))  #rightcard
	
		cutnum(imgBANKER,(69,1,92,32),'BANKER-middle.jpg')
		clr.print_blue_text(u"BANKER-当中是。。。。。"+str(getverify1('BANKER-middle.jpg')))  #middlecard
	
		cutnum(imgBANKER,((12,1,39,32)),'BANKER-left.jpg')
		clr.print_blue_text(u"BANKER-左边是。。。。。"+str(getverify1('BANKER-left.jpg')))  #leftcard




	

	




