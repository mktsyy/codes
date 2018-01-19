##memoryControlPic
#-*-coding:utf-8-*-

from io import BytesIO
from PIL import Image,ImageGrab
import os

f = BytesIO()
im = ImageGrab.grab() 
im.save(os.getcwd()+"/screenshot9999.png")
f.write("screenshot9999.png")

im1=Image.open(f.getvalue())
rec=((569,751,746,817))
region=im1.crop(rec)
# region.show()
region.save(os.getcwd()+'/'+"screenshot8888.jpg")