##remain
#-*-coding:utf-8-*-

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
from multiprocessing import Process


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
for i in xrange(210,256):
	for n in xrange(210,256):
		for g in xrange(210,256):
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

# 子进程要执行的代码
def run_proc(PlayPiccoordinate,PlayerPicName,PlayerLeftJudgeCoordinate,PlayerCutCoordinate,PlayerLeftPicName):
	while True:
		# print "PLAYER-left.jpg here"

		if PlayerPicName == "testnew.jpg" :
			time.sleep(0.2)
		else:
			time.sleep(0.5)
		


		cutpic(PlayPiccoordinate,PlayerPicName)
		img = Image.open(PlayerPicName)
		# print img.getpixel((23,23))
		
		tempx = []
		x = 0
		while x < len(PlayerLeftJudgeCoordinate):
			tempx.append(img.getpixel(PlayerLeftJudgeCoordinate[x]))
			# print type(img.getpixel(PlayerLeftJudgeCoordinate[x]))
			x = x + 1

		# print tempx
		# print len(list(set(tempx).intersection(set(ifcolor))))
		# print "PlayerLeftJudgeCoordinate........."+str(len(PlayerLeftJudgeCoordinate))
		##判断列表中元素是否在ifcolor中，如果一样，再进行截图操作
		if len(list(set(tempx).intersection(set(ifcolor)))) == len(PlayerLeftJudgeCoordinate):
			cutnum(img,(PlayerCutCoordinate),PlayerLeftPicName)
			leftpic = Image.open(PlayerLeftPicName)
			newLP = leftpic.rotate(270)
			newLP.save(PlayerLeftPicName)

			# if imgBANKER.getpixel((137,26)) in ifcolor:
			##先移除像素点值，便于只输出一次
			# playLeftColorRecode = img.getpixel(i)
			# ifcolor.remove(playLeftColorRecode)

			del PlayerLeftJudgeCoordinate[0]

			if "BANKER" in PlayerLeftPicName:
				clr.print_blue_text(PlayerLeftPicName.split('.')[0]+u"。。。。。"+str(getverify1(PlayerLeftPicName)))
			else:
				print PlayerLeftPicName.split('.')[0]+u"。。。。。"+str(getverify1(PlayerLeftPicName))  #leftcard

			##录屏
			im = ImageGrab.grab() 
			im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

			if PlayerLeftPicName == 'PLAYER-left.jpg':
				time.sleep(4)
			else:
				time.sleep(2)
			break
		else:
			break
		break
   

def ScreenShot():
	im = ImageGrab.grab() 
	im.save(os.getcwd()+"/screenshot.png")#保存图片 


if __name__=='__main__':
	##准备移除的像素点值做赋值
	colorRecorde = 0
	playLeftColorRecode = 0
	bankerRightRecode = 0
	while True:
		# print colorRecorde
		# print bankerRightRecode
		time.sleep(1)

		

		PLAYERLeftPic = Process(target=run_proc, args=((569,751,746,817),"testnew.jpg",[(23,23)],(0,30,34,53),'PLAYER-left.jpg'))
		BANKERRightPic = Process(target=run_proc, args=((1173,751,1350,817),"BANKER.jpg",[(175,63),(145,63),(165,54)],(112,30,144,54),'BANKER-right.jpg'))
		ScreenShotPic = Process(target=ScreenShot,args=())

		

		##PLAYER
		ScreenShotPic.start()
		ScreenShotPic.join()

		# cutpic((569,751,746,817),"testnew.jpg")
		# cutpic((1173,751,1350,817),"BANKER.jpg")

		PLAYERLeftPic.start()
		BANKERRightPic.start()
		PLAYERLeftPic.join()
		BANKERRightPic.join()

	

	

		img = Image.open("testnew.jpg")

		imgBANKER = Image.open("BANKER.jpg")
	
	# # print img.getpixel((23,23))
	# if img.getpixel((23,23)) in ifcolor:
	# 	cutnum(img,((0,30,34,53)),'PLAYER-left.jpg')
	# 	leftpic = Image.open('PLAYER-left.jpg')
	# 	newLP = leftpic.rotate(270)
	# 	newLP.save("PLAYER-left.jpg")

	# 	# if imgBANKER.getpixel((137,26)) in ifcolor:
	# 	##先移除像素点值，便于只输出一次
	# 	playLeftColorRecode = img.getpixel((23,23))
	# 	ifcolor.remove(playLeftColorRecode)

	# 	print u"PLAYER-左边是。。。。。"+str(getverify1('PLAYER-left.jpg'))  #leftcard

	# # print img.getpixel((137,26))
	# elif imgBANKER.getpixel((137,26)) in ifcolor:
	# 	cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
	# 	rightpic = Image.open('BANKER-right.jpg')
	# 	newRP = rightpic.rotate(270)
	# 	newRP.save("BANKER-right.jpg")
	# 	clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

	# 	bankerRightRecode = imgBANKER.getpixel((137,26))
	# 	ifcolor.remove(bankerRightRecode)


	# print playLeftColorRecode
	##把已移除的像素点值重新加入，方便下次再判断
	##原来的
	# if playLeftColorRecode <> 0 and colorRecorde <> 0 and bankerRightRecode <> 0 :

		if colorRecorde <> 0:
			time.sleep(12)
			ifcolor.append(colorRecorde)
			# ifcolor.append(playLeftColorRecode)
			# ifcolor.append(bankerRightRecode)
			colorRecorde = 0
			# playLeftColorRecode = 0
			# bankerRightRecode = 0
			clr.print_red_text('---------------------------------')
			continue

		elif img.getpixel((79,16))  not in ifcolor and imgBANKER.getpixel((62,26))   \
		not in ifcolor and img.getpixel((130,3)) not in ifcolor and imgBANKER.getpixel((7,26)) not in ifcolor and \
		imgBANKER.getpixel((137,26)) not in ifcolor and img.getpixel((23,23)) not in ifcolor:
			ifcolor.append(colorRecorde)
			# ifcolor.append(playLeftColorRecode)
			# ifcolor.append(bankerRightRecode)
			colorRecorde = 0
			# playLeftColorRecode = 0
			# bankerRightRecode = 0
			clr.print_red_text('---------------------------------')
			continue



		# print img.getpixel((79,16))
		elif img.getpixel((79,16))  in ifcolor  and imgBANKER.getpixel((62,26)) in ifcolor  \
		and img.getpixel((130,3)) in ifcolor and imgBANKER.getpixel((7,26)) in ifcolor:

			# print colorRecorde
			# print playLeftColorRecode

			cutnum(img,(86,1,111,30),'PLAYER-middle.jpg')
			print u"PLAYER-当中是。。。。。"+str(getverify1('PLAYER-middle.jpg'))  #middlecard

			cutnum(img,((138,1,167,31)),'PLAYER-right.jpg')
			print u"PLAYER-右边是。。。。。"+str(getverify1('PLAYER-right.jpg'))  #rightcard
		
			cutnum(imgBANKER,(69,1,92,32),'BANKER-middle.jpg')
			clr.print_blue_text(u"BANKER-当中是。。。。。"+str(getverify1('BANKER-middle.jpg')))  #middlecard
		
			cutnum(imgBANKER,((12,1,39,32)),'BANKER-left.jpg')
			clr.print_blue_text(u"BANKER-左边是。。。。。"+str(getverify1('BANKER-left.jpg')))  #leftcard

			##考虑到移除后不利于下次取值，所以还要加入判断是否移除
			## print clr.intCardNum(getverify1('PLAYER-middle.jpg'))
			# if clr.intCardNum(getverify1('PLAYER-middle.jpg')) + clr.intCardNum(getverify1('PLAYER-right.jpg')) < 6 \
			#    or clr.intCardNum(getverify1('BANKER-middle.jpg'))+clr.intCardNum(getverify1('BANKER-left.jpg')) < 6:
			####先移除像素点值，便于只输出一次
			colorRecorde = img.getpixel((79,16))
			ifcolor.remove(img.getpixel((79,16)))
			# time.sleep(15)


		##录屏
		# im = ImageGrab.grab() 
		# im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# if  clr.intCardNum(getverify1('PLAYER-middle.jpg')) + clr.intCardNum(getverify1('PLAYER-right.jpg')) > 10:
		# 	mainCard = clr.intCardNum(getverify1('PLAYER-middle.jpg')) + clr.intCardNum(getverify1('PLAYER-right.jpg')) -10
		# 	# print mainCard
		# else:
		# 	mainCard =  clr.intCardNum(getverify1('PLAYER-middle.jpg')) + clr.intCardNum(getverify1('PLAYER-right.jpg'))
		# # print mainCard

		# if clr.intCardNum(getverify1('BANKER-middle.jpg')) + clr.intCardNum(getverify1('BANKER-left.jpg')) > 10:
		# 	BankerCard = clr.intCardNum(getverify1('BANKER-middle.jpg')) + clr.intCardNum(getverify1('BANKER-left.jpg')) - 10
		# else:
		# 	BankerCard = clr.intCardNum(getverify1('BANKER-middle.jpg')) + clr.intCardNum(getverify1('BANKER-left.jpg'))

		
		# if mainCard <= 5:

			
		# 	# print BankerCard
		# 	# while True:
		# 	# 	print "PLAYER-left.jpg here"
		# 	# 	time.sleep(1.5)
		# 	# 	cutpic((569,751,746,817),"testnew.jpg")
		# 	# 	img = Image.open("testnew.jpg")
		# 	# 	# print img.getpixel((23,23))
		# 	# 	if img.getpixel((23,23)) in ifcolor:
		# 	# 		cutnum(img,((0,30,34,53)),'PLAYER-left.jpg')
		# 	# 		leftpic = Image.open('PLAYER-left.jpg')
		# 	# 		newLP = leftpic.rotate(270)
		# 	# 		newLP.save("PLAYER-left.jpg")

		# 	# 		# if imgBANKER.getpixel((137,26)) in ifcolor:
		# 	# 		##先移除像素点值，便于只输出一次
		# 	# 		playLeftColorRecode = img.getpixel((23,23))
		# 	# 		ifcolor.remove(playLeftColorRecode)
		# 	# 		print u"PLAYER-左边是。。。。。"+str(getverify1('PLAYER-left.jpg'))  #leftcard

		# 	# 		##录屏
		# 	# 		im = ImageGrab.grab() 
		# 	# 		im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# 	# 		# time.sleep(3)
		# 	# 		break

		# 	if BankerCard <=2:
		# 		while True:
		# 			print "BankerCard <=2 here"
		# 			time.sleep(1)
		# 			cutpic((1173,751,1350,817),"BANKER.jpg")
		# 			imgBANKER = Image.open("BANKER.jpg")
		# 			# print img.getpixel((137,26))
		# 			if imgBANKER.getpixel((175,63)) in ifcolor and imgBANKER.getpixel((114,20)) in ifcolor:
		# 				cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		# 				rightpic = Image.open('BANKER-right.jpg')
		# 				newRP = rightpic.rotate(270)
		# 				newRP.save("BANKER-right.jpg")
		# 				clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

		# 				bankerRightRecode = imgBANKER.getpixel((137,26))
		# 				ifcolor.remove(bankerRightRecode)

		# 				##录屏
		# 				im = ImageGrab.grab() 
		# 				im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# 				time.sleep(3)
		# 				break




		# 	if BankerCard == 3:

		# 		if clr.intCardNum(getverify1('PLAYER-left.jpg')) == 8:
		# 			time.sleep(3)
		# 			continue
		# 		else:

		# 			while True:
		# 				# print "here"
		# 				time.sleep(1.5)
		# 				cutpic((1173,751,1350,817),"BANKER.jpg")
		# 				imgBANKER = Image.open("BANKER.jpg")
		# 				# print img.getpixel((137,26))
		# 				if imgBANKER.getpixel((175,63)) in ifcolor and imgBANKER.getpixel((114,20)) in ifcolor:
		# 					cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		# 					rightpic = Image.open('BANKER-right.jpg')
		# 					newRP = rightpic.rotate(270)
		# 					newRP.save("BANKER-right.jpg")
		# 					clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

		# 					bankerRightRecode = imgBANKER.getpixel((137,26))
		# 					ifcolor.remove(bankerRightRecode)

		# 					##录屏
		# 					im = ImageGrab.grab() 
		# 					im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# 					time.sleep(3)
		# 					break

		# 	if BankerCard == 4 :
		# 		try:
		# 			if int(getverify1('PLAYER-left.jpg')) == 10 :
		# 				continue
		# 		except:
		# 				pass

		# 		if clr.intCardNum(getverify1('PLAYER-left.jpg')) == 1 or clr.intCardNum(getverify1('PLAYER-left.jpg')) == 8 or  \
		# 		clr.intCardNum(getverify1('PLAYER-left.jpg')) == 9 or clr.intCardNum(getverify1('PLAYER-left.jpg')) == 10:
		# 			time.sleep(3)
		# 			continue
		# 		else:
		# 			while True:
		# 				# print "here"
		# 				time.sleep(1.5)
		# 				cutpic((1173,751,1350,817),"BANKER.jpg")
		# 				imgBANKER = Image.open("BANKER.jpg")
		# 				# print img.getpixel((137,26))
		# 				if imgBANKER.getpixel((175,63)) in ifcolor and imgBANKER.getpixel((114,20)) in ifcolor:
		# 					cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		# 					rightpic = Image.open('BANKER-right.jpg')
		# 					newRP = rightpic.rotate(270)
		# 					newRP.save("BANKER-right.jpg")
		# 					clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

		# 					bankerRightRecode = imgBANKER.getpixel((137,26))
		# 					ifcolor.remove(bankerRightRecode)

		# 					##录屏
		# 					im = ImageGrab.grab() 
		# 					im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# 					break

		# 	if BankerCard == 5 :

		# 		try:
		# 			if int(getverify1('PLAYER-left.jpg')) == 10 :
		# 				continue
		# 		except:
		# 				pass

		# 		if clr.intCardNum(getverify1('PLAYER-left.jpg')) == 1 or clr.intCardNum(getverify1('PLAYER-left.jpg')) == 2 or  \
		# 		clr.intCardNum(getverify1('PLAYER-left.jpg')) == 3 or clr.intCardNum(getverify1('PLAYER-left.jpg')) == 8 or \
		# 		clr.intCardNum(getverify1('PLAYER-left.jpg')) == 9 or clr.intCardNum(getverify1('PLAYER-left.jpg')) == 10:
		# 			continue
		# 		else:
		# 			while True:
		# 				# print "here"
		# 				time.sleep(1.5)
		# 				cutpic((1173,751,1350,817),"BANKER.jpg")
		# 				imgBANKER = Image.open("BANKER.jpg")
		# 				# print img.getpixel((137,26))
		# 				if imgBANKER.getpixel((175,63)) in ifcolor and imgBANKER.getpixel((114,20)) in ifcolor:
		# 					cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		# 					rightpic = Image.open('BANKER-right.jpg')
		# 					newRP = rightpic.rotate(270)
		# 					newRP.save("BANKER-right.jpg")
		# 					clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

		# 					bankerRightRecode = imgBANKER.getpixel((137,26))
		# 					ifcolor.remove(bankerRightRecode)

		# 					##录屏
		# 					im = ImageGrab.grab() 
		# 					im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# 					break
			

			
		# 	else:
		# 		ifcolor.append(colorRecorde)
		# 		colorRecorde = 0
		# 		playLeftColorRecode = 0
		# 		bankerRightRecode = 0
		# 		clr.print_red_text('---------------------------------')
		# 		time.sleep(3)
		# 		continue
			


	 # 	elif mainCard == 6 or mainCard == 7 :

	 # 		if BankerCard <= 5 :
	 # 			while True:
		# 				time.sleep(1.5)
		# 				cutpic((1173,751,1350,817),"BANKER.jpg")
		# 				imgBANKER = Image.open("BANKER.jpg")
		# 				# print img.getpixel((137,26))
		# 				if imgBANKER.getpixel((175,63)) in ifcolor and imgBANKER.getpixel((114,20)) in ifcolor:
		# 					cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		# 					rightpic = Image.open('BANKER-right.jpg')
		# 					newRP = rightpic.rotate(270)
		# 					newRP.save("BANKER-right.jpg")
		# 					clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

		# 					bankerRightRecode = imgBANKER.getpixel((137,26))
		# 					ifcolor.remove(bankerRightRecode)

		# 					##录屏
		# 					im = ImageGrab.grab() 
		# 					im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 


		# 					break
		# 		continue
		# 	elif BankerCard == 6:
		# 		if clr.intCardNum(getverify1('PLAYER-left.jpg')) == 6 or clr.intCardNum(getverify1('PLAYER-left.jpg')) == 7:
		# 			while True:
		# 				# print "here"
		# 				time.sleep(1.5)
		# 				cutpic((1173,751,1350,817),"BANKER.jpg")
		# 				imgBANKER = Image.open("BANKER.jpg")
		# 				# print img.getpixel((137,26))
		# 				if imgBANKER.getpixel((175,63)) in ifcolor and imgBANKER.getpixel((114,20)) in ifcolor:
		# 					cutnum(imgBANKER,((112,30,144,54)),'BANKER-right.jpg')
		# 					rightpic = Image.open('BANKER-right.jpg')
		# 					newRP = rightpic.rotate(270)
		# 					newRP.save("BANKER-right.jpg")
		# 					clr.print_blue_text(u"BANKER-右边是。。。。。"+str(getverify1('BANKER-right.jpg')))  #rightcard

		# 					bankerRightRecode = imgBANKER.getpixel((137,26))
		# 					ifcolor.remove(bankerRightRecode)

		# 					##录屏
		# 					im = ImageGrab.grab() 
		# 					im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

		# 					break
		# 	else:
		# 		ifcolor.append(colorRecorde)
		# 		colorRecorde = 0
		# 		playLeftColorRecode = 0
		# 		bankerRightRecode = 0
		# 		clr.print_red_text('---------------------------------')
		# 		time.sleep(3.5)
		# 		continue


		# elif  mainCard == 8 or mainCard == 9:
		#  	time.sleep(2)
		#  	continue

		# else:
		#  	continue

	

	




