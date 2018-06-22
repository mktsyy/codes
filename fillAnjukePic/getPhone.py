##getPhone
# -*- coding: UTF-8 -*-
###识别有问题，待修正

from PIL import ImageGrab,Image,ImageEnhance
import pytesseract
import os

# 二值化    
threshold = 140    
table = []    
for i in range(256):    
    if i < threshold:    
        table.append(0)    
    else:    
        table.append(1) 

##抓取桌面全图
def ScreenShot():
	##直接抓坐标图，具体坐标可以用ps来查看
	im = ImageGrab.grab((749,142,844,159)) 
	print (im.size)
	# im.save(os.getcwd()+"/screenshot.png")#保存图片 
	# img = Image.open("screenshot.png")
	# img1 = img.crop((749,142,844,159))
	# img1.save(os.getcwd()+'/'+"test.png")
	im.save(os.getcwd()+'/'+"test.png")

ScreenShot()

image = Image.open('test.png')

##调整图片属性，使图片更易于辨认
enhancer = ImageEnhance.Color(image)
enhancer = enhancer.enhance(10)
# enhancer = ImageEnhance.Brightness(enhancer)
# enhancer = enhancer.enhance(2)
enhancer = ImageEnhance.Contrast(enhancer)
enhancer = enhancer.enhance(8)
enhancer = ImageEnhance.Sharpness(enhancer)
image = enhancer.enhance(20)

#转化到灰度图  
imgry = image.convert('L')  
#保存图像  
imgry.save('gtest.png')
#二值化，采用阈值分割法，threshold为分割点   
out = imgry.point(table,'1')    
out.save('btest.png')   
text = pytesseract.image_to_string(image)

##字符串中去空格方法
print("".join(text.split()))