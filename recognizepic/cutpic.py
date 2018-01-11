##cutpic
#-*-coding:utf-8-*-

from PIL import Image,ImageGrab
import os


def cutpic(coordinate,savename):
	# im = ImageGrab.grab() 
	# im.save(os.getcwd()+"/screenshot.png")#保存图片 
	im1=Image.open(os.getcwd()+"/screenshot.png")
	rec=(coordinate)
	region=im1.crop(rec)
	# region.show()
	region.save(os.getcwd()+'/'+savename)

def cutnum(img,coordinate,savename):
	region = (coordinate)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+'/'+savename)