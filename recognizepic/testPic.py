##testPIc

#-*-coding:utf-8-*-

from getPicture import *

def pic(savename,coordinate,picname):
	im1=Image.open(os.getcwd()+"\\pic\\"+picname)
	region=im1.crop((coordinate))
	region.save(os.getcwd()+'/'+savename)