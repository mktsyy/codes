#-*-coding:utf-8-*-
import win32gui,win32api
import win32con
import time
import PIL
from PIL import Image,ImageGrab
import os 

def main():
	print win32gui.GetCursorPos()

	#定位
	win32api.SetCursorPos([510,846])

	# 鼠标点击
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
	time.sleep(0.05)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	time.sleep(0.05)

if __name__ == '__main__':
	main()