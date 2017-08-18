#-*-coding:utf-8-*-
import win32gui
import PIL
from PIL import Image,ImageGrab
import os 


def main():
	print win32gui.GetCursorPos()
	# im = ImageGrab.grab() 
	# im.save(os.getcwd()+"/screenshot.png")#保存图片 
	# # #os.execvp( "mspaint",('mspaint','c:/screenshot.png'))#调用画图程序打开截屏图片
	# im1=Image.open(os.getcwd()+"/screenshot.png")
	# # print im1.size

	# rec=(679,713,806,760)
	# region=im1.crop(rec)
	# # # region.show()
	# region.save(os.getcwd()+"/123.bmp")
	# img = Image.open('123.bmp')

	# i = Image.open("123.bmp")
	# c = i.getpixel((31, 7))
	##颜色值(31, 55, 58)

	# i = Image.open("33333.bmp")
	# c = i.getpixel((31, 7))
	##颜色值(24, 74, 92)

	# i = Image.open("555543.bmp")
	# c = i.getpixel((31, 7))
	##颜色值(31, 54, 55)


	# i = Image.open("999999.bmp")
	# c = i.getpixel((31, 7))
	##颜色值(32, 54, 55)

	# i = Image.open("123.bmp")
	# c = i.getpixel((24, 16))
	# ##颜色值(232, 235, 235)

	# i = Image.open("123.bmp")
	# c = i.getpixel((19, 18))
	# # ##颜色值类黑色(89, 89, 90)

	i = Image.open("123.bmp")
	c = i.getpixel((9,33))
	# # ##颜色值黑色(0, 0, 0)
	print c

	# # #数字Q

	

	# region = (1,19,22,40)

	# cropImg = img.crop(region)

	# cropImg.save(os.getcwd()+"\\rightTemp\\rightQ.jpg")

if __name__ == '__main__':
	main()