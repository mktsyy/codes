##controlMouse
#-*-coding:utf-8-*-

from pynput.mouse import Button, Controller

mouse = Controller()

def positionClick():
	mouse.position = (1553, 840)
	mouse.click(Button.left, 2)

def writeCity():
	mouse.position = (553, 710)
	mouse.click(Button.left, 1)

def restore():
	mouse.position = (1240,676)
	mouse.click(Button.left,1)


print('The current pointer position is {0}'.format(
    mouse.position))