# #-*-coding:utf-8-*-
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

# #房屋户型-室
# # win32api.SetCursorPos([572,605])
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # time.sleep(0.05)
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # time.sleep(0.05)
# # #快捷键2
# # win32api.keybd_event(50,0,0,0)     
# # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# # #房屋户型 -厅
# # win32api.SetCursorPos([705, 607])
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # time.sleep(0.05)
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # time.sleep(0.05)
# # #快捷键2
# # win32api.keybd_event(50,0,0,0)     
# # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)


# # #房屋户型 -卫
# # win32api.SetCursorPos([817, 602])
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # time.sleep(0.05)
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # time.sleep(0.05)
# # #快捷键2
# # win32api.keybd_event(50,0,0,0)     
# # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# # #楼层 - 楼
# # win32api.SetCursorPos([594, 657])
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # time.sleep(0.05)
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # time.sleep(0.05)
# # #快捷键2
# # win32api.keybd_event(50,0,0,0)     
# # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# # #楼层 - 层
# # win32api.SetCursorPos([723, 656])
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # time.sleep(0.05)
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # time.sleep(0.05)
# # #快捷键2
# # win32api.keybd_event(50,0,0,0)     
# # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# # # #房屋情况 -1
win32api.SetCursorPos([632, 601])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.SetCursorPos([591, 670])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)


win32api.SetCursorPos([746, 608])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.SetCursorPos([746, 764])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)


# # # #出租间介绍
win32api.SetCursorPos([580, 655])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.SetCursorPos([560, 983])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

# # # #面积
# # # win32api.SetCursorPos([552, 739])
# # # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # # time.sleep(0.05)
# # # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # # time.sleep(0.05)
# # # #快捷键2
# # # win32api.keybd_event(50,0,0,0)     
# # # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# # # #配套设施 - 全选
win32api.SetCursorPos([564, 772])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

# # # #租金
# # # win32api.SetCursorPos([628, 947])
# # # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # # time.sleep(0.05)
# # # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # # time.sleep(0.05)
# # # #快捷键2
# # # win32api.keybd_event(50,0,0,0)     
# # # win32api.keybd_event(50,0,win32con.KEYEVENTF_KEYUP,0)

# # # ##付款方式
win32api.SetCursorPos([799, 925])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

#下
win32api.keybd_event(34,0,0,0)     
win32api.keybd_event(34,0,win32con.KEYEVENTF_KEYUP,0)
time.sleep(0.5)

win32api.SetCursorPos([780, 261])
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

# ##标题
# # win32api.SetCursorPos([820, 950])
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
# # time.sleep(0.05)
# # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
# # time.sleep(0.05)

##使用房源模板
win32api.SetCursorPos([975, 344])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)

win32api.SetCursorPos([828, 580])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)
win32api.SetCursorPos([901, 630])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.05)

## os.system("pause")
##上传室内图
win32api.SetCursorPos([616, 874])
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) 
time.sleep(0.05)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
time.sleep(0.5)

win32api.keybd_event(18,0,0,0)     # ALT
win32api.keybd_event(38,0,0,0)     # Up Arrow　
win32api.keybd_event(38,0,win32con.KEYEVENTF_KEYUP,0)     #Up Arrow　
win32api.keybd_event(18,0,win32con.KEYEVENTF_KEYUP,0)     #ALT
i = 1
while i<12:
	win32api.keybd_event(9,0,0,0)     # Tab 　　　　　　
	win32api.keybd_event(9,0,win32con.KEYEVENTF_KEYUP,0)     #Tab
	i+=1
win32api.keybd_event(40,0,0,0)     # Down Arrow 
win32api.keybd_event(40,0,win32con.KEYEVENTF_KEYUP,0)     #Down Arrow 
time.sleep(0.2)
win32api.keybd_event(13,0,0,0)     # Enter 
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)     #Enter 
time.sleep(0.2)
win32api.keybd_event(17,0,0,0)     # Control 　　　　 
win32api.keybd_event(65,0,0,0)     # A 
win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0)     #A 
win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)     #Control 　　　
win32api.keybd_event(13,0,0,0)     # Enter 
win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)     #Enter 



# ## 让Python遍历当前Windows下所有运行程序的窗口，并获得运行窗口的标题输出
# # from win32gui import *
# # titles = set()
# # def foo(hwnd,mouse):
# #  #去掉下面这句就所有都输出了，但是我不需要那么多
# # 	if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
# # 		titles.add(GetWindowText(hwnd))
# # EnumWindows(foo, 0)
# # lt = [t for t in titles if t]
# # lt.sort()
# # for t in lt:
# # 	print(t.decode('GB2312'))
