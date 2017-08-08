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


def bubble(l):
    flag = True
    for i in range(len(l)-1, 0, -1):
        if flag: 
            flag = False
            for j in range(i):
                if l[j] > l[j + 1]:
                    l[j], l[j+1] = l[j+1], l[j]
                    flag = True
        else:
            break
    return l


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

	cropImg.save(os.getcwd()+"\\temp\\10.jpg")

	#数字9

	region = (43,9,52,19)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\9.jpg")

	# #数字6
	region = (40,6,48,16)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\6.jpg")

	# #数字5


	region = (44,9,51,19)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\5.jpg")

	# #数字Q


	region = (43,9,52,18)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\Q.jpg")

	# #数字K


	region = (43,9,52,18)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\K.jpg")

	# #数字4


	region = (40,6,48,15)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\4.jpg")

	# #数字J


	region = (43,9,52,18)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\J.jpg")

	# #数字3

	region = (43,9,52,18)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\3.jpg")

	# #数字2

	region = (43,9,52,18)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\2.jpg")

	# #数字8

	region = (43,9,52,18)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\8.jpg")

	#数字A
	region = (39,6,49,15)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\A.jpg")

	#数字7

	region = (39,6,49,16)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\temp\\7.jpg")


	   
	################以下未完成      
	cutpic = os.listdir(os.getcwd()+"\\temp")
	# a=getImgHash("temp.jpg")#图片地址自行替换 
	comparelist = []
	secondcard = []
	for pic in cutpic:
		a=getImgHash(os.getcwd()+"\\temp\\"+pic)#图片地址自行替换 
		files = os.listdir(os.getcwd()+"\\num")#图片文件夹地址自行替换  

		#用ipython调试
		# from IPython import embed
		# embed()

		for file in files:
		   # print file
			if not file in"recognize.pycutpic.pyNpicrecognize.pycutpicsendcard.pycutpicfirstcard.pytempall.pynumtemp":
				b=getImgHash(os.getcwd()+"\\num\\"+file)  
				compare=getMH(a,b)  
				comparelist.append(int(compare)) 
				strdata = str(pic)+"............"+ file+u'相似度'+str(compare)+'%'
				secondcard.append(strdata)
				# print str(pic)+"............"+ file,u'相似度',str(compare)+'%'
		# print str(pic)+"............"+ file,u'最相似,相似度',str(max(comparelist))+'%'

	#用ipython调试
	# from IPython import embed
	# embed()	
	for ii in secondcard:
		if str(max(comparelist)) in ii:
			print ii.split(".bmp")[0].split(".jpg")[1]


if __name__ == '__main__':
	main()