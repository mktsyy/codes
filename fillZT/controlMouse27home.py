##controlMouse
#-*-coding:utf-8-*-
from pynput.mouse import Button, Controller

mouse = Controller()

def positionClick():
	mouse.position = (1438, 607)
	mouse.click(Button.left, 1)

def writeAddress():
	mouse.position = (1401, 652)
	mouse.click(Button.left, 1)

def writeCity():
	mouse.position = (612, 517)
	mouse.click(Button.left, 1)

def restore():
	mouse.position = (1661,365)
	mouse.click(Button.left,1)


print('The current pointer position is {0}'.format(
    mouse.position))