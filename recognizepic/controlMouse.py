##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import win32gui,win32api
import time


## print win32gui.GetCursorPos()

mouse = Controller()

##点击一元押注
def oneCoin(num):
	i = 0
	while i < num:
		mouse.position = (775, 1022)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		# time.sleep(0.1)

		####押注
		mouse.position = (1246, 843)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		# time.sleep(0.1)
		i = i + 1

##点击五元押注
def fiveCoin(num):
	i = 0
	while i < num:
		mouse.position = (830, 1000)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)

		# # ##押注
		mouse.position = (1246, 843)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		i = i + 1

#点击撤销
def resetCard():
	mouse.position = (706, 1044)
	mouse.press(Button.left)
	time.sleep(0.1)
	mouse.release(Button.left)
	mouse.press(Button.left)
	time.sleep(0.1)
	mouse.release(Button.left)


##test
oneCoin(2)
time.sleep(1)
resetCard()

# Read pointer position
print('The current pointer position is {0}'.format(
    mouse.position))

##选择一元
# mouse.position = (775, 1022)

# ##选择五元
# # mouse.position = (830, 1000)

# ##选择二十五元
# # mouse.position = (898, 987)

# ##选择一百元
# # mouse.position = (959, 986)

# mouse.press(Button.left)
# time.sleep(0.1)

# mouse.release(Button.left)

# time.sleep(0.1)

# # ##押注
# mouse.position = (1246, 843)

# mouse.press(Button.left)
# time.sleep(0.1)
# mouse.release(Button.left)
# # time.sleep(0.8)

##一次点击中没有延迟，不能用？？
# # mouse.click(Button.left, 1)

# ##取消
# time.sleep(0.1)

# mouse.position = (706, 1044)

# mouse.press(Button.left)
# time.sleep(0.1)
# mouse.release(Button.left)
# mouse.press(Button.left)
# time.sleep(0.1)
# mouse.release(Button.left)

