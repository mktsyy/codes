##controlMouse
#-*-coding:utf-8-*-

from pymouse import PyMouse
from pykeyboard import PyKeyboard
import win32gui,win32api
import time

m = PyMouse()
k = PyKeyboard()

print win32gui.GetCursorPos()

#定位
# win32api.SetCursorPos((812, 42))

##选择一元
m.click(775, 1022,n=2)
time.sleep(1)
##押注
m.click(1246, 843,n=2)

time.sleep(1)
m.click(706, 1044,n=2)