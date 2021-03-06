##Coroutine
#- * -coding: utf - 8 - * -
##识别训练方法http://www.cnblogs.com/samlin/p/Tesseract-OCR.html

from getPicture import *
 
# import ImageEnhance    
# import ImageFilter    
import sys    
from pytesser import *  ##调用GOOGLE识别模块
from recognizenum import * ##识牌模块
import time
from PIL import Image,ImageGrab
import when##更简单时间模块
import os
from multiprocessing import Process,Manager,Lock##多进程模块
import ctypes##python调用C模块
from controlMouse import *
from sendpicmail import sendPicMail
import Tkinter 


##隐藏dos窗口
import win32api, win32gui  
ct = win32api.GetConsoleTitle()  
hd = win32gui.FindWindow(0,ct)  
win32gui.ShowWindow(hd,0)

##ipython的步进调试
# from ipdb import set_trace
# set_trace()

##生成接近白色的颜色集
ifcolor = []
for i in xrange(210,256):
	for n in xrange(210,256):
		for g in xrange(210,256):
			ifcolor.append((i,n,g))

pointColor = []
for i in xrange(185,194):
	for n in xrange(176,185):
		for g in xrange(160,168):
			pointColor.append((i,n,g))
##用ie颜色变了，重新调整
# ifcolor = []
# for i in xrange(190,256):
# 	for n in xrange(180,256):
# 		for g in xrange(160,256):
# 			ifcolor.append((i,n,g))

		
##抓取桌面全图
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

# ##加入UI
root = Tkinter.Tk()
##tk中独有的变量
var = Tkinter.StringVar()

root.title ("Casino Recognize")
##窗口置顶
root.wm_attributes('-topmost',1)
##label标签设置文本变量
Tkinter.Label(root, textvariable = var).pack()



#生成牌总数列表
cardAllNum = []
k = 0
# print cardAllNum.count('A')
basicCard =['0','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
for i in basicCard:
	while k < 32:
		cardAllNum.append(i)
		k = k + 1
	k = 0

##加入c计算赔率  
class testdll(ctypes.Structure):  
    _fields_=[('Banker_wager',ctypes.c_int),  
             ('Player_wager',ctypes.c_int),
             ('Tie_wager',ctypes.c_int),
             ('Pair_wager',ctypes.c_int),
             ('DB_wager',ctypes.c_int),
             # ('DB_EV',ctypes.c_double),
             ] 

pDll=ctypes.WinDLL("test5.dll")
##其中sum是c的函数名称
pDll.Dec_bet.restype=testdll 


##dos下字体变色类
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

    ##原来是设定检测是否值不在允许值，现在没有用 
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

##生成颜色类
clr = Color()

##生成当中所有牌的生成器函数
def consumer():
	r = ''
	while True:
		n = yield r
		# print n
		if not n:
			return

		# print('[CONSUMER] Consuming %s...' % n)

		# ##from IPython import embed
		# ##embed()
		img = Image.open("testnew.jpg")

		imgBANKER = Image.open("BANKER.jpg")

		cutnum(img,(86,1,111,30),'PLAYER-middle.jpg')
		# ##from IPython import embed
		# ##embed()
		print u"PLAYER-当中是。。。。。"+str(getverify1('PLAYER-middle.jpg'))  #middlecard
		# ##from IPython import embed
		# ##embed()

		cutnum(img,((138,1,167,31)),'PLAYER-right.jpg')
		print u"PLAYER-右边是。。。。。"+str(getverify1('PLAYER-right.jpg'))  #rightcard
		
		cutnum(imgBANKER,((12,1,39,32)),'BANKER-left.jpg')
		clr.print_blue_text(u"BANKER-左边是。。。。。"+str(getverify1('BANKER-left.jpg')))  #leftcard

		cutnum(imgBANKER,(69,1,92,32),'BANKER-middle.jpg')
		clr.print_blue_text(u"BANKER-当中是。。。。。"+str(getverify1('BANKER-middle.jpg')))  #middlecard
		
		##生成器函数返回列表
		r = [str(getverify1('PLAYER-middle.jpg')),str(getverify1('PLAYER-right.jpg')),
		str(getverify1('BANKER-left.jpg')),str(getverify1('BANKER-middle.jpg'))]
		##from IPython import embed
		##embed()

##生成PLAYER-left.jpg的生成器函数
def consumer1():
	r = ''
	while True:
		n = yield r
		# print n
		if not n:
			return

		# print('[CONSUMER] Consuming %s...' % n)

		# ##from IPython import embed
		# ##embed()
		img = Image.open("testnew.jpg")

		imgBANKER = Image.open("BANKER.jpg")

		cutnum(img,((0,30,34,53)),'PLAYER-left.jpg')
		leftpic = Image.open('PLAYER-left.jpg')
		newLP = leftpic.rotate(270)
		newLP.save("PLAYER-left.jpg")
		print u"PLAYER-左边是。。。。。"+str(getverify1('PLAYER-left.jpg'))  #leftcard

		r = str(getverify1('PLAYER-left.jpg'))
		##from IPython import embed
		##embed()

##生成BANKER.jpg的生成器函数
def consumer2():
	r = ''
	while True:
		n = yield r
		# print n
		if not n:
			return

		# print('[CONSUMER] Consuming %s...' % n)

		# ##from IPython import embed
		# ##embed()
		img = Image.open("testnew.jpg")

		imgBANKER = Image.open("BANKER.jpg")

		##切图，生成单个图片
		cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		##图片旋转
		rightpic = Image.open('BANKER-right.jpg')
		newRP = rightpic.rotate(270)
		newRP.save("BANKER-right.jpg")
		##以蓝色字体打印
		clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard
		#生成器函数返回值
		r = str(getverify1('BANKER-right.jpg'))
		##from IPython import embed
		##embed()

def gogogo(name,num):
	oneCoin()
	if name == "Banker_wager":
		Banker_wager(num)
	elif name == "Player_wager":
		Player_wager(num)
	elif name == "DB_wager":
		DB_wager(num)
	elif name == "Tie_wager":
		Tie_wager(num)
	elif name == "Pair_wager":
		Pair_wager(num)
	sendPicMail("screenshot.png")

def produce(c,d,e):

	##生成器函数初始化
	c.send(None)
	d.send(None)
	e.send(None)
	#传递值初始化
	n = 0
	##锁定每个生成器函数值设置为0
	MAINCARD = 0
	PLAYLEFTCARD = 0
	BANKERRIGHTCARD = 0

	##延时押注，以避免进程检测(这个方法会有漏洞，不用)
	# xxxx = when.future(seconds = 600)

	##防止闲置变量
	spareTime = 0

	##开始循环检查是否已经开牌
	while True:

		
		n = n + 1
		# time.sleep(0.2)
		##截屏,原先所用延时方法会导致文件抢读取错误，现在用进程锁保证任务顺利执行完毕
		##
		# ScreenShotPic = Process(target=ScreenShot,args=())
		# ScreenShotPic.start()
		# ScreenShotPic.join()
		ScreenShot()
		time.sleep(0.2)

		#点击确定在此桌
		clickDevice()

		##分辨切PLAYER和BANKER和牌重置的图
		cutpic((569,751,746,817),"testnew.jpg")
		cutpic((1173,751,1350,817),"BANKER.jpg")
		cutpic((1468,121,1485,138),"Point.jpg")

		##Screenimg
		Screenimg = Image.open("Point.jpg")

		##PLAYERimg
		img = Image.open("testnew.jpg")

		##BANKERimg
		imgBANKER = Image.open("BANKER.jpg")
		
		##插入ipython断点，待进入循环时停止检查变量
		##from IPython import embed
		##embed()

		##定时押注，默认为10分钟一次防呆滞(有漏洞，弃用)
		# if when.now() == xxxx:
		# 	oneCoin()
		# 	Player_wager(1)
		# 	xxxx = when.now()

		#检查是否又是新牌，如果新牌的话，重置牌数
		if Screenimg.getpixel((13,9))  in pointColor and Screenimg.getpixel((8,14))  in pointColor:
			del cardAllNum[:] 
			k = 0
			# print cardAllNum.count('A')
			basicCard =['0','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
			for i in basicCard:
				while k < 32:
					cardAllNum.append(i)
					k = k + 1
				k = 0

			##延时点击重置(有漏洞，弃用)
			# xxxx = when.future(seconds = 600)

		##检查是否桌面已清空，清空的话每处归零
		if MAINCARD != 0 and img.getpixel((79,16))  not in ifcolor and imgBANKER.getpixel((62,26))   \
		not in ifcolor and img.getpixel((130,3)) not in ifcolor and imgBANKER.getpixel((7,26)) not in ifcolor and \
		imgBANKER.getpixel((137,26)) not in ifcolor and img.getpixel((23,23)) not in ifcolor:
			MAINCARD = 0
			PLAYLEFTCARD = 0
			BANKERRIGHTCARD = 0

			# #当中点击一下，防锁定
			clickmiddle()

			##防止闲置
			spareTime = spareTime + 1

			if spareTime == 12:
				oneCoin()
				Player_wager(1)
				spareTime = 0 

			##打印剩余牌数目
			clr.print_red_text('---------------------------------')
			print clr.print_green_text([
			'0'+':'+str(cardAllNum.count('0')), 
			'A'+':'+str(cardAllNum.count('A')), 
			'2'+':'+str(cardAllNum.count('2')), 
			'3'+':'+str(cardAllNum.count('3')), 
			'4'+':'+str(cardAllNum.count('4')),
			'5'+':'+str(cardAllNum.count('5')), 
			'6'+':'+str(cardAllNum.count('6')), 
			'7'+':'+str(cardAllNum.count('7')), 
			'8'+':'+str(cardAllNum.count('8')), 
			'9'+':'+str(cardAllNum.count('9')), 
			'10'+':'+str(cardAllNum.count('10')), 
			'J'+':'+str(cardAllNum.count('J')), 
			'Q'+':'+str(cardAllNum.count('Q')), 
			'K'+':'+str(cardAllNum.count('K'))
			]) 
			clr.print_red_text('---------------------------------')

			# ##UI显示
			Uilist = \
			'0'+':'+str(cardAllNum.count('0'))+',\n' \
			+  'A'+':'+str(cardAllNum.count('A'))+',\n' \
			+  '2'+':'+str(cardAllNum.count('2'))+',\n' \
			+  '3'+':'+str(cardAllNum.count('3'))+',\n' \
			+  '4'+':'+str(cardAllNum.count('4'))+',\n' \
			+ '5'+':'+str(cardAllNum.count('5'))+',\n' \
			+  '6'+':'+str(cardAllNum.count('6'))+',\n' \
			+  '7'+':'+str(cardAllNum.count('7'))+',\n' \
			+  '8'+':'+str(cardAllNum.count('8'))+',\n' \
			+  '9'+':'+str(cardAllNum.count('9'))+',\n' \
			+  '10'+':'+str(cardAllNum.count('10'))+',\n' \
			+  'J'+':'+str(cardAllNum.count('J'))+',\n' \
			+  'Q'+':'+str(cardAllNum.count('Q'))+',\n' \
			+  'K'+':'+str(cardAllNum.count('K'))+',\n' \
			+ 'Total :'+str(len(cardAllNum)-32)
			
			var.set(str(Uilist))
			root.update()

			

			#打印当前时间
			print when.now()

			##准备c的ARRAY准备传入dll做运算
			finallist = [
					cardAllNum.count('0'), 
					cardAllNum.count('A'), 
					cardAllNum.count('2'), 
					cardAllNum.count('3'), 
					cardAllNum.count('4'),
					cardAllNum.count('5'), 
					cardAllNum.count('6'), 
					cardAllNum.count('7'), 
					cardAllNum.count('8'), 
					cardAllNum.count('9'), 
					cardAllNum.count('10'), 
					cardAllNum.count('J'),
					cardAllNum.count('Q'), 
					cardAllNum.count('K')
					]
			# print finallist
			#生成14个变量的ARRAY
			m = (ctypes.c_int *14)(*finallist)

			import numpy as np
			arraytolist = np.array(m)
			# print arraytolist.tolist()

			t=pDll.Dec_bet(m) 

			print t.Banker_wager  
			print t.Player_wager
			print t.DB_wager
			print t.Tie_wager
			print t.Pair_wager
			# print t.DB_EV

			wagerlist = {"t.Banker_wager":t.Banker_wager, "t.Player_wager":t.Player_wager, "t.DB_wager":t.DB_wager, "t.Tie_wager":t.Tie_wager, "t.Pair_wager":t.Pair_wager}

			for wagerName,wagerValue in wagerlist.items():
				if wagerValue > 0:
					time.sleep(1)
					gogogo (wagerName.split('.')[1],wagerValue)
					


			clr.print_red_text('---------------------------------')

		##检测当中的四张牌
		if MAINCARD == 0 and img.getpixel((79,16))  in ifcolor  and imgBANKER.getpixel((62,26)) in ifcolor  \
		and img.getpixel((130,3)) in ifcolor and imgBANKER.getpixel((7,26)) in ifcolor \
		and imgBANKER.getpixel((2,3)) in ifcolor and imgBANKER.getpixel((103,3)) in ifcolor:
			r = c.send(n)
			MAINCARD = r
			# print ('[PRODUCER] Consumer return: %s' % str(r))
			for i in r:
				cardAllNum.remove(i)

		##检查PLAYER的最左面牌
		if PLAYLEFTCARD == 0 and img.getpixel((23,23)) in ifcolor:
			r1 = d.send(n)
			PLAYLEFTCARD = r1
			cardAllNum.remove(r1)
			# print ('[PRODUCER] Consumer return: %s' % r1)

		##检查BANKER的最后面牌
		if BANKERRIGHTCARD == 0 and imgBANKER.getpixel((137,26)) in ifcolor:
			r2 = e.send(n)
			BANKERRIGHTCARD = r2
			cardAllNum.remove(r2)
			##from IPython import embed
			##embed()
		# r = c.send(n)
		# print('[PRODUCER] Consumer return: %s' % r)	
		
	c.close()

##主进程，生成三个生成器函数，开始循环检查
def main():
	c = consumer()
	d = consumer1()
	e = consumer2()
	produce(c,d,e)
	
if __name__ == '__main__':
	main()