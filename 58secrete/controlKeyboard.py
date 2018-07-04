##controlKeyboard
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.keyboard import Key, Controller

keyboard = Controller()

def keyFill(phone):
	keyboard.type(phone)

def space():
	i=30
	while i > 0:
		keyboard.press(Key.backspace)
		keyboard.release(Key.backspace)
		i = i - 1

def enter():
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)
	