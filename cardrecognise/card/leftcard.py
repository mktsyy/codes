#leftall
#-*-coding:utf-8-*-

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
	# print win32gui.GetCursorPos()
	# im = ImageGrab.grab() 
	# im.save(os.getcwd()+"/screenshot.png")#保存图片 
	# #os.execvp( "mspaint",('mspaint','c:/screenshot.png'))#调用画图程序打开截屏图片
	# im1=Image.open(os.getcwd()+"/screenshot.png")
	# print im1.size

	# rec=(800,840,880,875)
	# region=im1.crop(rec)
	# # region.show()
	# region.save(os.getcwd()+"/123.bmp")

	img = Image.open('123.bmp')

	#数字7

	

	region = (5,15,18,26)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left7.jpg")

	#数字A

	

	region = (6,16,15,26)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\leftA.jpg")

	#数字K

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\leftK.jpg")

	#数字4

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left4.jpg")

	#数字2

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left2.jpg")

	#数字3

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left3.jpg")

	#数字5

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left5.jpg")

	#数字6

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left6.jpg")

	#数字8

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left8.jpg")

	#数字9

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left9.jpg")

	#数字J

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\leftJ.jpg")

	#数字Q

	

	region = (6,17,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\leftQ.jpg")

	#数字10

	

	region = (6,16,15,25)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\lefttemp\\left10.jpg")

	################以下完成      
	cutpic = os.listdir(os.getcwd()+"\\lefttemp")
	# a=getImgHash("temp.jpg")#图片地址自行替换 
	comparelist = []
	secondcard = []
	for pic in cutpic:
		a=getImgHash(os.getcwd()+"\\lefttemp\\"+pic)#图片地址自行替换 
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
			print (u"最左位......."+ii)


if __name__ == '__main__':
	main()