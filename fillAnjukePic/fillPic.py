##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import win32gui,win32api
import time
from controlKeyboard import doKeyboard,altUp,down,enter,LaoGongTV,ctrlTab,ctrlW,space,ctrlV,keyFill
import sys
import when
import win32con  
import win32clipboard as w 

mouse = Controller()

def setText(aString):  
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)  
    w.CloseClipboard() 

def fillInnerPicFirst():
	mouse.position = (649, 512)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (180, 187)
	mouse.click(Button.left, 1)
	time.sleep(0.5)
	mouse.position = (866, 649)
	mouse.click(Button.left, 2)
	time.sleep(0.5)
	mouse.position = (334, 110)
	mouse.click(Button.left, 2)
	time.sleep(0.5)
	mouse.position = (1041, 442)
	mouse.click(Button.left, 2)
	mouse.scroll(-100,-500)
	time.sleep(0.5)
	mouse.position = (324, 208)
	mouse.click(Button.left, 2)
	time.sleep(0.5)
	mouse.position = (707, 339)
	mouse.click(Button.left, 2)
	doKeyboard()
	time.sleep(0.5)
	mouse.position = (1074, 739)
	mouse.click(Button.left, 2)

def fillInnerPicSecond():
	mouse.position = (649, 512)
	mouse.click(Button.left, 1)
	time.sleep(0.2)
	altUp()
	time.sleep(0.2)
	mouse.position = (323, 668)
	mouse.click(Button.left, 1)
	# time.sleep(0.5)
	down()
	enter()
	time.sleep(0.1)
	doKeyboard()
	time.sleep(0.5)
	mouse.position = (1074, 739)
	mouse.click(Button.left, 2)

def signLaoGongTV():
	mouse.position = (1738,969)
	mouse.click(Button.left,1)
	LaoGongTV()
	enter()

def clickSendRoom():
	# ctrlTab()
	mouse.position = (273,518)
	mouse.click(Button.left,1)
	space()
	space()
	space()
	time.sleep(1)
	mouse.position = (583,775)
	mouse.click(Button.left,1)
	time.sleep(3)
	ctrlW()

def HZmobilBroker(username,password):

	##点击删除用户名
	mouse.position = (1022,292)
	mouse.click(Button.left,1)
	time.sleep(0.2)

	##粘帖用户名
	mouse.position = (897,293)
	mouse.click(Button.left,1)
	ctrlV()
	time.sleep(0.2)
	mouse.position = (894,326)
	mouse.click(Button.left,1)
	time.sleep(0.2)
	setText(password)
	time.sleep(0.5)

	##删除密码
	mouse.position = (1022,326)
	mouse.click(Button.left,1)

	##粘帖密码
	mouse.position = (889,328)
	mouse.click(Button.left,1)
	# time.sleep(2)
	ctrlV()

	##点击登录
	time.sleep(0.2)
	mouse.position = (958,393)
	mouse.click(Button.left,1)

def sendMessages(msg):
	oldPosition = mouse.position
	mouse.position = (837,949)
	mouse.click(Button.left,1)
	time.sleep(0.2)
	keyFill(msg)
	time.sleep(0.8)
	mouse.position = (1188,946)
	mouse.click(Button.left,1)
	time.sleep(0.2)
	mouse.position = (734,110)
	mouse.click(Button.left,1)
	mouse.position = (736,444)

def signOutApp():
	mouse.position = (1164,949)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	mouse.position = (1074,568)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	mouse.position = (947,376)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	mouse.position = (1141,570)
	mouse.click(Button.left,1)

def fillPhone(phone):
	mouse.position = (862,167)
	mouse.click(Button.left,2)
	time.sleep(0.5)
	mouse.position = (1165,110)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	mouse.position = (835,500)
	mouse.click(Button.left,1)
	keyFill(phone)
	time.sleep(0.5)
	mouse.position = (849,547)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	keyFill(phone)
	time.sleep(0.5)
	mouse.position = (944,633)
	mouse.click(Button.left,1)
	# time.sleep(0.5)
	# mouse.position = (737,106)
	# mouse.click(Button.left,1)

def sendDX():
	mouse.position = (749,948)
	mouse.click(Button.left,2)
	time.sleep(0.5)
	mouse.position = (1079,612)
	mouse.click(Button.left,1)
	time.sleep(5)
	mouse.position = (735,111)
	mouse.click(Button.left,1)

def HZadmin():
	##记住原来位置
	oldPosition = mouse.position
	##选择页面区域
	mouse.position = (1112,649)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	space()
	space()
	space()
	space()
	space()
	time.sleep(0.5)
	##点击下一页
	mouse.position = (1607,1005)
	mouse.click(Button.left,1)
	time.sleep(0.5)

	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''
	//发送后台发布成功房源数目
	var _alert =window.alert;
	window.alert = function(){

	    //把字符串分割便于发送到web后端进行处理
	    var aa = arguments[0].split("成功发布")[1].split("套")[0];
	    //区域值传递到后台进行处理
	    var region = document.getElementsByName("region")[0].value;

	    console.log(aa);

	    function showHint() {
	        var xmlhttp;

	        if (window.XMLHttpRequest) {
	            // IE7+, Firefox, Chrome, Opera, Safari 浏览器执行代码
	            xmlhttp = new XMLHttpRequest();
	        } else {
	            // IE6, IE5 浏览器执行代码
	            xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
	        }
	        xmlhttp.onreadystatechange = function() {
	            if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
	                // var value = json.parse(xmlhttp.responseText)
	                alert(xmlhttp.responseText);
	            }
	        }
	        xmlhttp.open("GET", "http://127.0.0.1:8000/HZadmin/?HZalert=" + aa + "&region=" + region, true);
	        xmlhttp.send();
	        
	    }

	    showHint();

	    // _alert(argu ments[0]);
	}

	'''
	setText(codes)
	ctrlV()
	enter()

	mouse.position = (259,463)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	##恢复原位置
	mouse.position = oldPosition

	



# fillInnerPicFirst()
# fillInnerPicSecond()

##带参数运行python命令
# print sys.argv

if len(sys.argv)>1:
	if list(sys.argv)[1] == "Second":
		fillInnerPicSecond()
	elif list(sys.argv)[1] == "First":
		fillInnerPicFirst()
	elif list(sys.argv)[1] == "lg":
		while True:
			signLaoGongTV()
			print (when.now())
			time.sleep(601)
	elif list(sys.argv)[1] == "cr":
		while True:
			clickSendRoom()
			print (when.now())
			time.sleep(30)
	elif list(sys.argv)[1] == "hz":
		HZadmin()

print('The current pointer position is {0}'.format(
    mouse.position))