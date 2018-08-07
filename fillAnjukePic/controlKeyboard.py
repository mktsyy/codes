##controlKeyboard
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.keyboard import Key, Controller

keyboard = Controller()

def doKeyboard():
	with keyboard.pressed(Key.ctrl):
		keyboard.press('a')
		keyboard.release('a')

def doKeyboardc():
	with keyboard.pressed(Key.ctrl):
		keyboard.press('c')
		keyboard.release('c')

def doKeyboardv():
	with keyboard.pressed(Key.ctrl):
		keyboard.press('v')
		keyboard.release('v')

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

def LaoGongTV():
	keyboard.type("#打卡")

def ctrlTab():
	with keyboard.pressed(Key.ctrl):
		keyboard.press(Key.tab)
		keyboard.release(Key.tab)

def ctrlW():
	with keyboard.pressed(Key.ctrl):
		keyboard.press("w")
		keyboard.release("w")

def ctrlC():
	with keyboard.pressed(Key.ctrl):
		keyboard.press("c")
		keyboard.release("c")

def ctrlV():
	with keyboard.pressed(Key.ctrl):
		keyboard.press("v")
		keyboard.release("v")

def space():
	keyboard.press(Key.space)
	keyboard.release(Key.space)

def keyFill(phone):
	keyboard.type(phone)

def ctrlShiftI():
	with keyboard.pressed(Key.ctrl):
		keyboard.press(Key.shift)
		keyboard.press("i")
		keyboard.release(Key.shift)
		keyboard.release("i")

def ctrlShiftTab():
	with keyboard.pressed(Key.ctrl):
		keyboard.press(Key.shift)
		keyboard.press(Key.tab)
		keyboard.release(Key.shift)
		keyboard.release(Key.tab)