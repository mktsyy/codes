
# coding: utf-8

from pynput import mouse
from controlKeyboard import doKeyboard,doKeyboardv,doKeyboardc
import time
# import win32api
# import win32con

mouse1 = mouse.Controller()

def on_move(x, y):
	print('Pointer moved to {0}'.format(
		(x, y)))

def on_click(x, y, button, pressed):
	# print('{0} at {1}'.format(
	# 	'Pressed' if pressed else 'Released',
	# 	(x, y)))

	
	# doKeyboardc()
	# doKeyboardv()
	print (str(button))
	if pressed and str(button) == "Button.left" :
		# win32api.keybd_event(17,0,0,0)     # Control 　　　　 
		# win32api.keybd_event(65,0,0,0)     # A 
		# win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)     #A 
		# win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)     #Control 
		doKeyboard()
		time.sleep(0.1)
		doKeyboardc()
		time.sleep(0.1)
		doKeyboardv()
		

	if not pressed:
		# Stop listener
		return False



def on_scroll(x, y, dx, dy):
	print('Scrolled {0} at {1}'.format( 'down' if dy < 0 else 'up', (x, y)))

# Collect events until released
def reStart():
	with mouse.Listener(
			# on_move=on_move,
			on_click=on_click,

			# on_scroll=on_scroll) as listener:
			# on_scroll=on_scroll
			) as listener:
		listener.join()
		# return True

while True:
	reStart()
	# if reStart():
	#     reStart()
	# else:
	#     ##如果点击鼠标，那就认为监听失效，休息10秒
	#     time.sleep(10)
	#     print ('it is False')

