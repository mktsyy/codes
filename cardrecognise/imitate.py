#-*-coding:utf-8-*-
import win32gui
import PIL
from PIL import Image,ImageGrab
import os 


def main():
	print win32gui.GetCursorPos()
	im = ImageGrab.grab() 
	im.save(os.getcwd()+"/screenshot.png")#保存图片 
	#os.execvp( "mspaint",('mspaint','c:/screenshot.png'))#调用画图程序打开截屏图片
	im1=Image.open(os.getcwd()+"/screenshot.png")
	print im1.size

	rec=(800,840,880,875)
	region=im1.crop(rec)
	# region.show()
	region.save(os.getcwd()+"/123.bmp")

if __name__ == '__main__':
	main()