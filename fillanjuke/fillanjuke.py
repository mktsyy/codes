#-*-coding:utf-8-*-
import os
import time
import win32gui
import win32api
import win32con
import time

#os.startfile("D:\\artcut6\\Prog\\Artcut6.exe")
#time.sleep(1)

wdname1=u"房源发布 - 租房 - 中国网络经纪人 - Cent Browser"
w1hd=win32gui.FindWindow(0,wdname1)


# print w2hd

def active():
	 #获取窗口焦点
	w2hd=win32gui.FindWindowEx(w1hd,None,None,None)
	win32gui.SetForegroundWindow(w2hd)
	# time.sleep(0.2)

	# win32api.keybd_event(18,0,0,0)     # ALT
	# win32api.keybd_event(38,0,0,0)     # Up Arrow　
	# win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)     #Up Arrow　
	# win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)     #ALT
	# time.sleep(0.1)
	# i = 1
	# while i<10:
	# 	win32api.keybd_event(9,0,0,0)     # Tab 　　　　　　
	# 	win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)     #Tab
	# 	i+=1
	# # time.sleep(0.2)
	# # win32api.keybd_event(9,0,0,0)     # Tab 　　　　　　
	# # win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)     #Tab
	# win32api.keybd_event(40,0,0,0)     # Down Arrow 
	# win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)     #Down Arrow 
	# time.sleep(0.1)
	# win32api.keybd_event(13,0,0,0)     # Enter 
	# win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)     #Enter 
	# time.sleep(0.1)
	# win32api.keybd_event(17,0,0,0)     # Control 　　　　 
	# win32api.keybd_event(65,0,0,0)     # A 
	# win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)     #A 
	# win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)     #Control 　　　　 
	# win32api.keybd_event(13,0,0,0)     # Enter 
	# win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)     #Enter 



# if w1hd:
# 	print w1hd
# 	active()

# wdname1=u"房源发布 -租房 -中国网络经纪人 -Cent Browser"
# w1hd=win32gui.FindWindow(0,wdname1)

# active()


#获取当前坐标
print win32gui.GetCursorPos()

#让Python遍历当前Windows下所有运行程序的窗口，并获得运行窗口的标题输出
# from win32gui import *
# titles = set()
# def foo(hwnd,mouse):
#  #去掉下面这句就所有都输出了，但是我不需要那么多
# 	if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
# 		titles.add(GetWindowText(hwnd))
# EnumWindows(foo, 0)
# lt = [t for t in titles if t]
# lt.sort()
# for t in lt:
# 	print(t.decode('GB2312'))
