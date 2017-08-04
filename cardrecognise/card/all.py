#-*-coding:utf-8-*-
import win32gui
import PIL
from PIL import Image,ImageGrab
import os 
import pytesseract  
from pytesser import *  
from PIL import Image,ImageEnhance,ImageFilter  
import fnmatch  
import re,time  
import urllib, random 

#import hashlib    
   
def getGray(image_file):  
   tmpls=[]  
   for h in range(0,  image_file.size[1]):#h  
      for w in range(0, image_file.size[0]):#w  
         tmpls.append( image_file.getpixel((w,h))  )  
            
   return tmpls  
   
def getAvg(ls):#获取平均灰度值  
   return sum(ls)/len(ls)  
   
def getMH(a,b):#比较100个字符有几个字符相同  
   dist = 0;  
   for i in range(0,len(a)):  
      if a[i]==b[i]:  
         dist=dist+1  
   return dist  
   
def getImgHash(fne):  
   image_file = Image.open(fne) # 打开  
   image_file=image_file.resize((12, 12))#重置图片大小我12px X 12px  
   image_file=image_file.convert("L")#转256灰度图  
   Grayls=getGray(image_file)#灰度集合  
   avg=getAvg(Grayls)#灰度平均值  
   bitls=''#接收获取0或1  
   #除去变宽1px遍历像素  
   for h in range(1,  image_file.size[1]-1):#h  
      for w in range(1, image_file.size[0]-1):#w  
         if image_file.getpixel((w,h))>=avg:#像素的值比较平均值 大于记为1 小于记为0  
            bitls=bitls+'1'  
         else:  
            bitls=bitls+'0'  
   return bitls  
'''''          
   m2 = hashlib.md5()    
   m2.update(bitls) 
   print m2.hexdigest(),bitls 
   return m2.hexdigest() 
'''  

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

	img = Image.open('123.bmp')

	#数字10参数
	region = (38,5,50,16)

	cropImg = img.crop(region)

	cropImg.save("/temp/10.jpg")

	#数字9

	region = (40,6,49,16)

	cropImg = img.crop(region)

	cropImg.save("/temp/9.jpg")

	#数字6

	

	region = (40,6,48,16)

	cropImg = img.crop(region)

	cropImg.save("/temp/6.jpg")

	#数字5


	region = (41,6,48,16)

	cropImg = img.crop(region)

	cropImg.save("/temp/5.jpg")

	#数字Q


	region = (40,6,49,15)

	cropImg = img.crop(region)

	cropImg.save("/temp/Q.jpg")

	#数字K


	region = (40,6,48,15)

	cropImg = img.crop(region)

	cropImg.save("/temp/K.jpg")

	#数字4


	region = (40,6,48,15)

	cropImg = img.crop(region)

	cropImg.save("/temp/4.jpg")

	#数字J


	region = (41,6,48,16)

	cropImg = img.crop(region)

	cropImg.save("/temp/J.jpg")

	#数字3

	region = (41,6,48,16)

	cropImg = img.crop(region)

	cropImg.save("/temp/3.jpg")



	   
	################以下未完成      

	a=getImgHash("temp.jpg")#图片地址自行替换  
	files = os.listdir(os.getcwd())#图片文件夹地址自行替换  
	for file in files:
	   # print file
	   if not file in"recognize.pycutpic.pyNpicrecognize.pycutpicsendcard.pycutpicfirstcard.pytempall.py":
	      b=getImgHash(str(file))  
	      compare=getMH(a,b)  
	      print file,u'相似度',str(compare)+'%'

if __name__ == '__main__':
	main()