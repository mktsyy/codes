##testmultiprocessing
#- * -coding: utf - 8 - * -


from multiprocessing import Process
import os
from getPicture import *
from PIL import Image,ImageGrab
import when
import time
from pytesser import *  
from recognizenum import *

ifcolor = []
for i in xrange(210,256):
	for n in xrange(210,256):
		for g in xrange(210,256):
			ifcolor.append((i,n,g))

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

			print PlayerLeftPicName.split('.')[0]+u"。。。。。"+str(getverify1(PlayerLeftPicName))  #leftcard

			##录屏
			im = ImageGrab.grab() 
			im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

			if PlayerLeftPicName == 'PLAYER-left.jpg':
				time.sleep(5)
			else:
				time.sleep(3)
			break
		else:
			break
		break
   

def ScreenShot():
	im = ImageGrab.grab() 
	im.save(os.getcwd()+"/screenshot.png")#保存图片 
		
		

if __name__=='__main__':
	while True:
		time.sleep(1)
		# print('Parent process %s.' % os.getpid())
		PLAYERLeftPic = Process(target=run_proc, args=((569,751,746,817),"testnew.jpg",[(23,23)],(0,30,34,53),'PLAYER-left.jpg'))
		BANKERRightPic = Process(target=run_proc, args=((1173,751,1350,817),"BANKER.jpg",[(175,63),(145,63),(165,54)],(112,30,144,54),'BANKER-right.jpg'))
		ScreenShotPic = Process(target=ScreenShot,args=())
		# print('Child process will start.')
		ScreenShotPic.start()
		ScreenShotPic.join()
		PLAYERLeftPic.start()
		BANKERRightPic.start()
		PLAYERLeftPic.join()
		BANKERRightPic.join()
		# print('Child process end.')