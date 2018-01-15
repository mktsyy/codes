##testmultiprocessing
#- * -coding: utf - 8 - * -


from multiprocessing import Process,active_children,Pool
import os
from getPicture import *
from PIL import Image,ImageGrab
import when
import time
from pytesser import *  
from recognizenum import *
import ctypes

ifcolor = []
for i in xrange(210,256):
	for n in xrange(210,256):
		for g in xrange(210,256):
			ifcolor.append((i,n,g))

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

# 子进程要执行的代码
def run_proc(PlayPiccoordinate,PlayerPicName,PlayerLeftJudgeCoordinate,PlayerCutCoordinate,PlayerLeftPicName):

	clr = Color()

	# print PlayerLeftPicName

	# while True:
		# time.sleep(1)
	# 	# print "PLAYER-left.jpg here"
		# print PlayerLeftPicName

		## if PlayerPicName == "testnew.jpg" :
		## 	time.sleep(2)
		## 	break
		## else:
		## 	time.sleep(1)

	if PlayerPicName == "testnew.jpg" :
		time.sleep(0.2)
	else:
		time.sleep(1)
	
	##准备加入当中牌识别，这里是判断是否切图
	if PlayPiccoordinate == 0:
		pass
	else:
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

		if "PLAYER-middle" in PlayerLeftPicName or "PLAYER-right" in PlayerLeftPicName \
		 or "BANKER-middle" in PlayerLeftPicName or "BANKER-left"  in PlayerLeftPicName:
			pass


		if 'PLAYER-left.jpg' in PlayerLeftPicName or 'BANKER-right.jpg' in PlayerLeftPicName:
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

		return str(getverify1(PlayerLeftPicName))

		# if PlayerLeftPicName == 'PLAYER-left.jpg':
		# 	time.sleep(5)
		# elif PlayerLeftPicName == 'PLAYER-middle.jpg':
		# 	time.sleep(20)
		# elif PlayerLeftPicName == 'BANKER-left.jpg':
		# 	time.sleep(12)
		# elif PlayerLeftPicName == 'PLAYER-right.jpg':
		# 	time.sleep(10)
		# elif PlayerLeftPicName == 'BANKER-middle.jpg':
		# 	time.sleep(8)
		# else:
		# 	time.sleep(3)
		# break
	# else:
	# 	break
	# break
	return PlayerLeftPicName.split('.')[0]+" is run.........."
   

def ScreenShot():
	im = ImageGrab.grab() 
	im.save(os.getcwd()+"/screenshot.png")#保存图片 
		
		

if __name__=='__main__':
	while True:
		pool = Pool(processes=2)
		result = []
		time.sleep(1)
		# PLAYERmiddlePic = Process(target=run_proc, args=((569,751,746,817),"testnew.jpg",[(79,16)],(86,1,111,30),'PLAYER-middle.jpg'))
		# PLAYERLeftPic = Process(target=run_proc, args=((569,751,746,817),"testnew.jpg",[(23,23)],(0,30,34,53),'PLAYER-left.jpg'))
		# BANKERRightPic = Process(target=run_proc, args=((1173,751,1350,817),"BANKER.jpg",[(175,63),(145,63),(165,54)],(112,30,144,54),'BANKER-right.jpg'))
		ScreenShotPic = Process(target=ScreenShot,args=())
		ScreenShotPic.start()
		ScreenShotPic.join()

		# print pool.apply_async(run_proc, ((569,751,746,817),"testnew.jpg",[(23,23)],(0,30,34,53),'PLAYER-left.jpg'))
		result.append(pool.apply_async(run_proc, ((569,751,746,817),"testnew.jpg",[(23,23)],(0,30,34,53),'PLAYER-left.jpg')))
		result.append(pool.apply_async(run_proc, ((1173,751,1350,817),"BANKER.jpg",[(175,63),(145,63),(165,54)],(112,30,144,54),'BANKER-right.jpg')))


		pool.close()
		# pool.join()

		for res in result:
			# print ":::", res.get()
			if res.get() in "12345678910JQKA":
				time.sleep(4)
			# print res.get()



		# PLAYERmiddlePic.start()
		# PLAYERLeftPic.start()
		# BANKERRightPic.start()
		# # # PLAYERmiddlePic.join()
		# # print PLAYERLeftPic.is_alive()
		# # print BANKERRightPic.is_alive()
		# # for p in active_children():
		# #         print("child   p.name:" + p.name + "\tp.id" + str(p.pid))
		# PLAYERLeftPic.join()
		# # if  PLAYERLeftPic.is_alive():
		# # 	pass
		# # else:
		# # BANKERRightPic.terminate()
		# # PLAYERLeftPic.terminate()

		# # BANKERRightPic.terminate()

		# BANKERRightPic.join()

	

