##controlMouse
#-*-coding:utf-8-*-

from pynput.mouse import Button, Controller
import win32gui,win32api
import time


## print win32gui.GetCursorPos()

mouse = Controller()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

##选择一元
mouse.position = (775, 1022)

##选择五元
mouse.position = (830, 1000)

##选择二十五元
# mouse.position = (898, 987)

##选择一百元
# mouse.position = (959, 986)

mouse.press(Button.left)
time.sleep(0.3)
mouse.release(Button.left)

time.sleep(0.3)

# ##押注
mouse.position = (1246, 843)

mouse.press(Button.left)
time.sleep(0.3)
mouse.release(Button.left)
# time.sleep(0.8)
# mouse.click(Button.left, 1)

##取消
time.sleep(0.3)

mouse.position = (706, 1044)

mouse.press(Button.left)
time.sleep(0.3)
mouse.release(Button.left)
mouse.press(Button.left)
time.sleep(0.3)
mouse.release(Button.left)

