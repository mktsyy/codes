##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import time
from controlKeyboard import keyFill,space,enter


mouse = Controller()

def position(username,password):
	mouse.position = (969, 523)
	mouse.click(Button.left, 1)
	time.sleep(2)
	mouse.position = (1064, 491)
	mouse.click(Button.left, 1)
	space()
	keyFill(username)
	time.sleep(0.3)
	mouse.position = (916, 558)
	mouse.click(Button.left, 2)
	keyFill(password)
	time.sleep(0.3)
	mouse.position = (953, 638)
	mouse.click(Button.left, 2)

def posMes(mes):
	##发送客服消息
	mouse.position = (1118, 721)
	mouse.click(Button.left, 1)
	keyFill(mes)
	time.sleep(0.5)
	enter()

def exita():
	mouse.position = (1766, 1060)
	mouse.click(Button.right, 1)
	time.sleep(0.2)
	mouse.position = (1727, 1003)
	mouse.click(Button.left, 1)
	mouse.position = (1406, 488)
	
def exitaMI():
	mouse.position = (1671, 1060)
	mouse.click(Button.right, 1)
	time.sleep(0.2)
	mouse.position = (1584, 1003)
	mouse.click(Button.left, 1)
	mouse.position = (1406, 488)

def positionMI(username,password):
	mouse.position = (969, 523)
	mouse.click(Button.left, 1)
	time.sleep(1)
	mouse.position = (1064, 491)
	mouse.click(Button.left, 1)
	space()
	keyFill(username)
	time.sleep(0.3)
	mouse.position = (916, 558)
	mouse.click(Button.left, 2)
	keyFill(password)
	time.sleep(0.3)
	mouse.position = (953, 638)
	mouse.click(Button.left, 2)



print('The current pointer position is {0}'.format(
    mouse.position))