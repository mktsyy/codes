##controlMouse
#-*-coding:utf-8-*-
##这个是关于1920*1080分辨率的

from pynput.mouse import Button, Controller
import win32gui,win32api
import time
from controlKeyboard import doKeyboard,altUp,down,enter,LaoGongTV,ctrlTab,ctrlW,space,ctrlV,keyFill,ctrlShiftI
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
	##有优惠券
	# mouse.position = (1074,568)
	##正常
	mouse.position = (844,483)
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

	
def HZadminSolo():
	##记住原来位置
	oldPosition = mouse.position
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.1)

	##发送ctrlshifti
	ctrlShiftI()
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

	##设置代码至剪贴板，并粘帖发送
	setText(codes)
	ctrlV()
	enter()

	mouse.position = (259,463)
	mouse.click(Button.left,1)
	# time.sleep(0.5)
	#恢复原位置
	mouse.position = oldPosition

def HZadminPublic():
	##原发布账号勾选方法，采用javascript，但有多选择问题，暂时废弃
	mouse.position = (433,403)
	mouse.click(Button.left,1)
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''
	function select(num){
		for (var i = num.length - 1; i >= 0; i--) {
		document.getElementsByName("userid[]")[num[i]].checked = true;
		}
	}


	//读取区域以匹配电话号码(上海)
	var region = Number(document.getElementsByName("region")[0].value);
	switch (region) {
	    case 24:
	        // document.getElementsByName("userid[]")[2].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[2].nextSibling.nodeValue;
	        select([2,]);
	        break;
	    case 43:
	        // document.getElementsByName("userid[]")[8].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[8].nextSibling.nodeValue;
	        select([8,]);
	        break;
	    case 53:
	        // document.getElementsByName("userid[]")[0].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[0].nextSibling.nodeValue;
	        // document.getElementsByName("userid[]")[14].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[14].nextSibling.nodeValue;
	        select([0,14]);
	        break;
	    case 97:
	        // document.getElementsByName("userid[]")[13].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[13].nextSibling.nodeValue;
	        select([13,]);
	        break;
	    case 108:
	        // document.getElementsByName("userid[]")[6].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[6].nextSibling.nodeValue;
	        select([6,]);
	        break;
	    case 121:
	        // document.getElementsByName("userid[]")[1].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[1].nextSibling.nodeValue;
	        // document.getElementsByName("userid[]")[15].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[15].nextSibling.nodeValue;
	        select([1,15]);
	        break;
	    case 140:
	        // document.getElementsByName("userid[]")[9].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[9].nextSibling.nodeValue;
	        select([9,]);
	        break;
	    case 147:
	        // document.getElementsByName("userid[]")[5].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[5].nextSibling.nodeValue;
	        // document.getElementsByName("userid[]")[17].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[17].nextSibling.nodeValue;
	        select([5,17]);
	        break;
	    case 166:
	        // document.getElementsByName("userid[]")[4].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[4].nextSibling.nodeValue;
	        // document.getElementsByName("userid[]")[18].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[18].nextSibling.nodeValue;
	        select([4,18]);
	        break;
	    case 177:
	        // document.getElementsByName("userid[]")[3].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[3].nextSibling.nodeValue;
	        // document.getElementsByName("userid[]")[16].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[16].nextSibling.nodeValue;
	        select([3,16]);
	        break;
	    case 215:
	        // document.getElementsByName("userid[]")[7].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[7].nextSibling.nodeValue;
	        select([7,]);
	        break;
	    case 1:
	        // document.getElementsByName("userid[]")[7].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[7].nextSibling.nodeValue;
	        select([1,]);
	        break;
	    case 2:
	        // document.getElementsByName("userid[]")[7].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[7].nextSibling.nodeValue;
	        select([2,]);
	        break;
	    case 2:
	        // document.getElementsByName("userid[]")[7].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[7].nextSibling.nodeValue;
	        select([2,]);
	        break;
	    case 0:
	        // document.getElementsByName("userid[]")[7].nextSibling.nodeValue = "@" + document.getElementsByName("userid[]")[7].nextSibling.nodeValue;
	        select([0,]);
	        break;

	}

	'''
	setText(codes)
	ctrlV()
	time.sleep(0.2)
	enter()

	##至发布按钮处
	mouse.position = (881,777)
	mouse.click(Button.left,1)

def newPublic(coordinate):
	##记住原来位置
	oldPosition = mouse.position
	##点击发布
	mouse.position = (433,403)
	mouse.click(Button.left,1)
	# print (type(coordinate))
	time.sleep(0.5)
	##根据发布源勾选账号
	if coordinate == "长宁:18674586768":
		mouse.position = (987,589)
		mouse.click(Button.left,1)
	elif coordinate == "徐汇:13795419927":
		mouse.position = (988,515)
		mouse.click(Button.left,1)
	elif coordinate == "浦东:13296760994":
		mouse.position = (766,518)
		mouse.click(Button.left,1)
	elif coordinate == "浦东:嗨住全国12":
		mouse.position = (987,663)
		mouse.click(Button.left,1)
	elif coordinate == "杨浦:嗨住全国11":
		mouse.position = (878,664)
		mouse.click(Button.left,1)
	elif coordinate == "普陀:18202158542":
		mouse.position = (770,590)
		mouse.click(Button.left,1)
	elif coordinate == "闵行:13641026605":
		mouse.position = (877,519)
		mouse.click(Button.left,1)
	elif coordinate == "闵行:嗨住全国13":
		mouse.position = (766,699)
		mouse.click(Button.left,1)
	elif coordinate == "闸北:18768113824":
		mouse.position = (765,625)
		mouse.click(Button.left,1)
	elif coordinate == "宝山:15136289152":
		mouse.position = (988,554)
		mouse.click(Button.left,1)
	elif coordinate == "宝山:嗨住全国15":
		mouse.position = (987,698)
		mouse.click(Button.left,1)
	elif coordinate == "嘉定:15026518260":
		mouse.position = (877,554)
		mouse.click(Button.left,1)
	elif coordinate == "嘉定:嗨住全国16":
		mouse.position = (768,735)
		mouse.click(Button.left,1)
	elif coordinate == "松江:13810794175":
		mouse.position = (768,555)
		mouse.click(Button.left,1)
	elif coordinate == "松江:嗨住全国14":
		mouse.position = (877,699)
		mouse.click(Button.left,1)
	elif coordinate == "青浦:18670107293":
		mouse.position = (876,589)
		mouse.click(Button.left,1)
	elif coordinate == "朝阳&丰台:嗨住2017":
		mouse.position = (877,516)
		mouse.click(Button.left,1)
	elif coordinate == "海淀&大兴:嗨住2018":
		mouse.position = (987,515)
		mouse.click(Button.left,1)
	elif coordinate == "郑州:上海高度公司":
		mouse.position = (765,515)
		mouse.click(Button.left,1)

	##至发布按钮处
	# mouse.position = (881,777)
	# mouse.click(Button.left,1)

	##3秒后关闭
	time.sleep(3)
	ctrlW()

	#恢复原位置
	mouse.position = oldPosition

def cityMouse(http):
	mouse.position = (1068,48)
	mouse.click(Button.left,1)
	keyFill(http)
	enter()

def counterNum():
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.1)
	##发送ctrlshifti
	ctrlShiftI()
	time.sleep(0.5)
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''

	//统计数量打印在console口
	var k = 0;
	for (var i = document.getElementsByClassName("ck").length - 1; i >= 0; i--) {
	    if (document.getElementsByClassName("ck")[i].parentNode.parentNode.childNodes[13].childNodes[3].attributes[1].value == 'opt-link batchproyx') {
	    	console.log(k);
	    	k = k + 1;
		    }

	};
	'''
	setText(codes)
	ctrlV()
	time.sleep(0.2)
	enter()

def selectCancel(num1):
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''

	//统计数量打印在console口
	var k = 0;
	for (var i = document.getElementsByClassName("num").length - 2; i >= 0; i--) {
	if(k == %s){break;}
		if (Number(document.getElementsByClassName("num")[i].innerText.split("/")[0])==0 &&
			Number(document.getElementsByClassName("num")[i].innerText.split("/")[1])==0) {
			document.getElementsByClassName("num")[i].parentNode.childNodes[1].childNodes[1].checked = true;
			k = k + 1;
			console.log(k);
			
		}
		
	}

	
	//翻页绑定左右按键

	document.onkeydown = function(event) {
	    var e = event || window.event || arguments.callee.caller.arguments[0];  
	    if (e && e.keyCode == 39) {
	        document.getElementsByClassName("ui-multipage-next-active")[0].click();
	    } else if (e && e.keyCode == 37) {
	        document.getElementsByClassName("ui-multipage-pre-active")[0].click();
	    }
	};
	''' % str(num1)
	setText(codes)
	ctrlV()
	time.sleep(0.2)
	enter()

def firstSendCancle():
	##记住原来位置
	oldPosition = mouse.position

	mouse.position = (417,483)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	mouse.position = (518,489)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	mouse.position = (823,621)
	mouse.click(Button.left,1)
	time.sleep(0.8)
	mouse.position = (1205,861)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	
	#恢复原位置
	mouse.position = oldPosition

def dueCancle():
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''
	if(document.getElementsByClassName("lastday")){
	for (var i = document.getElementsByClassName("lastday").length - 1; i >= 0; i--) {
	document.getElementsByClassName("lastday")[i].parentNode.parentNode.parentNode.childNodes[1].childNodes[1].checked = true;
	}
	console.log(document.getElementsByClassName("lastday").length)
	}

	'''
	setText(codes)
	ctrlV()
	time.sleep(0.2)
	enter()

def GJdueCancle():
	##点击右面空白console处
	mouse.position = (1735,520)
	mouse.click(Button.left,1)
	time.sleep(0.5)
	codes = '''
	if(document.getElementsByClassName("lastday")){
	for (var i = document.getElementsByClassName("lastday").length - 1; i >= 0; i--) {
	document.getElementsByClassName("lastday")[i].parentNode.parentNode.parentNode.childNodes[1].childNodes[1].checked = true;
	}
	console.log(document.getElementsByClassName("lastday").length)
	}

	'''
	setText(codes)
	ctrlV()
	time.sleep(0.2)
	enter()

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