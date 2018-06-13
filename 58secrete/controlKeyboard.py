##controlKeyboard
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.keyboard import Key, Controller

keyboard = Controller()

def keyFill(phone):
	keyboard.type(phone)

	