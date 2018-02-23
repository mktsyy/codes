##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import win32gui,win32api
import time
from controlKeyboard import doKeyboard,altUp,down,enter
import sys

mouse = Controller()

def fillInnerPicFirst():
	mouse.position = (649, 512)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (180, 187)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (866, 649)
	mouse.click(Button.left, 2)
	time.sleep(0.5)
	mouse.position = (334, 110)
	mouse.click(Button.left, 2)
	time.sleep(0.5)
	mouse.position = (1041, 442)
	mouse.click(Button.left, 2)
	mouse.scroll(-100,-500)
	time.sleep(0.5)
	mouse.position = (324, 208)
	mouse.click(Button.left, 2)
	time.sleep(0.5)
	mouse.position = (707, 339)
	mouse.click(Button.left, 2)
	doKeyboard()
	time.sleep(0.5)
	mouse.position = (1074, 739)
	mouse.click(Button.left, 2)

def fillInnerPicSecond():
	mouse.position = (649, 512)
	mouse.click(Button.left, 1)
	time.sleep(0.2)
	altUp()
	time.sleep(0.2)
	mouse.position = (323, 668)
	mouse.click(Button.left, 1)
	# time.sleep(0.5)
	down()
	enter()
	time.sleep(0.1)
	doKeyboard()
	time.sleep(0.5)
	mouse.position = (1074, 739)
	mouse.click(Button.left, 2)



# fillInnerPicFirst()
# fillInnerPicSecond()

##带参数运行python命令
# print sys.argv

if len(sys.argv)>1:
	if list(sys.argv)[1] == "Second":
		fillInnerPicSecond()
	elif list(sys.argv)[1] == "First":
		fillInnerPicFirst()
print('The current pointer position is {0}'.format(
    mouse.position))