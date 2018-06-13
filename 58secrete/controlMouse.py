##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import time
from controlKeyboard import keyFill


mouse = Controller()

def position(username,password):
	mouse.position = (1164, 298)
	mouse.click(Button.left, 1)
	time.sleep(0.2)
	mouse.position = (861, 483)
	mouse.click(Button.left, 1)
	keyFill(username)
	time.sleep(0.5)
	mouse.position = (857, 532)
	mouse.click(Button.left, 2)
	keyFill(password)
	time.sleep(0.5)
	mouse.position = (953, 638)
	mouse.click(Button.left, 2)



print('The current pointer position is {0}'.format(
    mouse.position))