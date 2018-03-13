##controlMouse
#-*-coding:utf-8-*-

from pynput.mouse import Button, Controller

mouse = Controller()

def positionClick():
	mouse.position = (1584, 818)
	mouse.click(Button.left, 1)

def writeCity():
	mouse.position = (871, 686)
	mouse.click(Button.left, 1)

def restore():
	mouse.position = (1661,365)
	mouse.click(Button.left,1)


print('The current pointer position is {0}'.format(
    mouse.position))