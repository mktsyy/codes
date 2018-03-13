##ctrl_alt_clickleft
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.keyboard import Key, Controller
import pynput
import time

keyboard = Controller()

def doKeyboard():
	with keyboard.pressed(Key.ctrl):
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)
	pynput.mouse.Controller().click(pynput.mouse.Button.left, 1)


while True:
	time.sleep(0.5)
	doKeyboard()


