#-*-coding:utf-8-*-
import os
import time
import win32gui
import win32api
import win32con
import time


wdname1=u"房源发布 - 租房 - 中国网络经纪人 - Cent Browser"
w1hd=win32gui.FindWindow(0,wdname1)

#获取窗口焦点
w2hd=win32gui.FindWindowEx(w1hd,None,None,None)
win32gui.SetForegroundWindow(w2hd)
time.sleep(0.2)




# #获取当前坐标
print win32gui.GetCursorPos()

#房屋户型-室
# win32api.SetCursorPos([572,605])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# #房屋户型 -厅
# win32api.SetCursorPos([705, 607])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)


# #房屋户型 -卫
# win32api.SetCursorPos([817, 602])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# #楼层 - 楼
# win32api.SetCursorPos([594, 657])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# #楼层 - 层
# win32api.SetCursorPos([723, 656])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# #房屋情况 -1
win32api.SetCursorPos([574, 627])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.SetCursorPos([575, 694])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)


win32api.SetCursorPos([799, 632])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.SetCursorPos([734, 789])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)


# #出租间介绍
win32api.SetCursorPos([570, 678])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.SetCursorPos([570, 1003])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

# #面积
# win32api.SetCursorPos([552, 739])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# #配套设施 - 全选
win32api.SetCursorPos([561, 796])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

# #租金
# win32api.SetCursorPos([628, 947])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)
# #快捷键2
# win32api.keybd_event(50,0,0,0)     
# win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# ##付款方式
win32api.SetCursorPos([820, 950])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

#下
win32api.keybd_event(34,0,0,0)     
win32api.keybd_event(34,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(0.5)

win32api.SetCursorPos([763, 312])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

##标题
# win32api.SetCursorPos([820, 950])
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# time.sleep(0.05)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# time.sleep(0.05)



## 让Python遍历当前Windows下所有运行程序的窗口，并获得运行窗口的标题输出
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
