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
			time.sleep(1.1)
		else:
			time.sleep(0.8)
		


		cutpic(PlayPiccoordinate,PlayerPicName)
		img = Image.open(PlayerPicName)
		# print img.getpixel((23,23))
		for i in PlayerLeftJudgeCoordinate:

			if img.getpixel(i) in ifcolor:
				cutnum(img,(PlayerCutCoordinate),PlayerLeftPicName)
				leftpic = Image.open(PlayerLeftPicName)
				newLP = leftpic.rotate(270)
				newLP.save(PlayerLeftPicName)

				# if imgBANKER.getpixel((137,26)) in ifcolor:
				##先移除像素点值，便于只输出一次
				# playLeftColorRecode = img.getpixel(i)
				# ifcolor.remove(playLeftColorRecode)
				print PlayerLeftPicName.split('.')[0]+u"。。。。。"+str(getverify1(PlayerLeftPicName))  #leftcard

				##录屏
				im = ImageGrab.grab() 
				im.save(os.getcwd()+"\\pic\\"+str(when.now()).split(".")[0].replace(":","-")+"screenshot.png")#保存图片 

				# time.sleep(3)
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
		p = Process(target=run_proc, args=((569,751,746,817),"testnew.jpg",[(23,23)],(0,30,34,53),'PLAYER-left.jpg'))
		p1 = Process(target=run_proc, args=((1173,751,1350,817),"BANKER.jpg",[(175,63),(145,63)],(112,30,144,54),'BANKER-right.jpg'))
		p2 = Process(target=ScreenShot,args=())
		# print('Child process will start.')
		p2.start()
		p2.join()
		p.start()
		p1.start()
		p.join()
		p1.join()
		# print('Child process end.')