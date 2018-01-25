##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import win32gui,win32api
import time


## print win32gui.GetCursorPos()

mouse = Controller()


####押注
def Banker_wager(num):
	i = 0
	while i < num:
		mouse.position = (1246, 843)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		# time.sleep(0.1)
		i = i + 1

##点击一元
def oneCoin():
	mouse.position = (775, 1022)
	mouse.press(Button.left)
	time.sleep(0.1)
	mouse.release(Button.left)
	# time.sleep(0.1)

		

##点击五元押注
def fiveCoin():
	mouse.position = (830, 1000)
	mouse.press(Button.left)
	time.sleep(0.1)
	mouse.release(Button.left)


#点击撤销
def resetCard():
	i=0
	mouse.position = (706, 1044)
	while i < 10:
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		i = i + 1

def DB_wager(num):
	i = 0
	while i < num:
		# # ##押注
		mouse.position = (423, 640)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		i = i + 1

def Pair_wager(num):
	i = 0
	while i < num:
		# # ##押注
		mouse.position = (449, 885)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		mouse.position = (1471, 882)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		i = i + 1

def Tie_wager(num):
	i = 0
	while i < num:
		# # ##押注
		mouse.position = (985, 837)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		i = i + 1

def Player_wager(num):
	i = 0
	while i < num:
		# # ##押注
		mouse.position = (643, 819)
		mouse.press(Button.left)
		time.sleep(0.1)
		mouse.release(Button.left)
		i = i + 1

def clickmiddle():
	mouse.position = (958, 532)
	mouse.press(Button.left)
	time.sleep(0.1)
	mouse.release(Button.left)

def clickDevice():
	mouse.position = (923, 417)
	mouse.press(Button.left)
	time.sleep(0.1)
	mouse.release(Button.left)
	
##test
# oneCoin()

# time.sleep(0.1)
# Player_wager(2)
# time.sleep(1)
# resetCard()

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

