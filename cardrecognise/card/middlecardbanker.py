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

##导入dos字体变色
import ctypes

##pytesser安装方法，把pytesser下载，放入python的Lib\site-packages下，然后在
# Lib\site-packages\pytesser下新建空__init__.py文件，完成安装

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

def cmpcolor(coordinate):
	img = Image.open('123.bmp')
	if cmp(img.getpixel(coordinate),(236, 239, 237))==0 or cmp(img.getpixel(coordinate),(0, 0, 0))==0 \
	or cmp(img.getpixel(coordinate),(67, 94, 77))==0 or cmp(img.getpixel(coordinate),(63, 100, 89))==0 \
	or cmp(img.getpixel(coordinate),(233, 240, 243))==0:
		return True
	else:
		return False

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


def main():
	# #print win32gui.GetCursorPos()
	# im = ImageGrab.grab() 
	# im.save(os.getcwd()+"/screenshot.png")#保存图片 
	# #os.execvp( "mspaint",('mspaint','c:/screenshot.png'))#调用画图程序打开截屏图片


	im1=Image.open(os.getcwd()+"/screenshot.png")
	# print im1.size
	rec=(1173,751,1350,817)
	region=im1.crop(rec)
	# region.show()
	region.save(os.getcwd()+"/banker123.bmp")

	img = Image.open('banker123.bmp')
	print img.getpixel((2,6))

	# ##用ipython调试
	# from IPython import embed
	# embed()

	# if cmpcolor((2,6)) or cmpcolor((2,12)) or cmpcolor((2,10)) or cmpcolor((2,14)):
	

	#数字7

	

	region = (69,1,91,30)

	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle7.jpg")

	#数字A

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middleA.jpg")

	#数字K

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middleK.jpg")

	#数字4

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle4.jpg")

	#数字2

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle2.jpg")

	#数字3

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle3.jpg")

	#数字5

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle5.jpg")

	#数字6

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle6.jpg")

	#数字8

	

	region = (69,1,91,30)
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle8.jpg")

	#数字9

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle9.jpg")

	#数字J

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middleJ.jpg")

	#数字Q

	

	region = (69,1,91,30) 
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middleQ.jpg")

	#数字10

	

	region = (69,1,93,30)
	cropImg = img.crop(region)

	cropImg.save(os.getcwd()+"\\bankermiddletemp\\middle10.jpg")

	################以下完成      
	cutpic = os.listdir(os.getcwd()+"\\bankermiddletemp")
	# a=getImgHash("temp.jpg")#图片地址自行替换 
	comparelist = []
	secondcard = []
	lastlist = []
	for pic in cutpic:
		a=getImgHash(os.getcwd()+"\\bankermiddletemp\\"+pic)#图片地址自行替换 
		files = os.listdir(os.getcwd()+"\\num")#图片文件夹地址自行替换  

		#用ipython调试
		# from IPython import embed
		# embed()

		for file in files:
		   # print file
			if not file in"recognize.pycutpic.pyNpicrecognize.pycutpicsendcard.pycutpicfirstcard.pytempall.pynumtempleftcard.py":
				b=getImgHash(os.getcwd()+"\\num\\"+file)  
				compare=getMH(a,b)  
				comparelist.append(int(compare)) 
				strdata = str(pic)+"............"+ file+u'相似度'+str(compare)+'%'
				secondcard.append(strdata)
				# print str(pic)+"............"+ file,u'相似度',str(compare)+'%'
		# if int(max(comparelist))< 75:
		# 	print u"没有识别"
		# else:
		# 	print str(pic)+"............"+ file,u'最相似,相似度',str(max(comparelist))+'%'

	##用ipython调试
	## from IPython import embed
	## embed()	

	for ii in secondcard:
		if str(max(comparelist)) in ii:
			# print('\033[1;33;40m')
			if int(max(comparelist))> 75:
				# print (u"PLAYER当中位......."+ii.split(".bmp")[0].split("............")[1])
				lastlist.append(u"BANKER当中位......."+ii.split(".bmp")[0].split("............")[1])

	if (len(lastlist)>=1):
		clr = Color()
		clr.print_blue_text(lastlist[0])
		# print lastlist[0]

if __name__ == '__main__':
	# main()
	while True:
		time.sleep(0.1)
		main()