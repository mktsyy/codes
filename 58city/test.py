#-*-coding:utf-8-*-

from pynput.mouse import Button, Controller
import time
import win32clipboard as w 
import win32con 
from controlKeyboard import doKeyboard,altUp,down,enter,LaoGongTV,ctrlTab,ctrlW,space,ctrlV,keyFill,ctrlShiftI

mouse = Controller()

def setText(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard() 

for i in range(100):
	
	mouse.position = (1702,1006)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''
	document.getElementsByClassName("p-txt")[%s].innerText;
	''' % str(i)
	setText(codes)
	ctrlV()
	# time.sleep(2)
	enter()