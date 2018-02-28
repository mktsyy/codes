##controlKeyboard
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.keyboard import Key, Controller

keyboard = Controller()

def doKeyboard():
	with keyboard.pressed(Key.ctrl):
		keyboard.press('a')
		keyboard.release('a')

def altUp():
	with keyboard.pressed(Key.alt):
		keyboard.press(Key.up)
		keyboard.release(Key.up)

def down():
	keyboard.press(Key.down)
	keyboard.release(Key.down)

def enter():
	keyboard.press(Key.enter)
	keyboard.release(Key.enter)

def doKeyboardc():
	with keyboard.pressed(Key.ctrl):
		keyboard.press('c')
		keyboard.release('c')

def doKeyboardv():
	with keyboard.pressed(Key.ctrl):
		keyboard.press('v')
		keyboard.release('v')