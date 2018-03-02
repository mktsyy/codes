
# -*- coding: utf-8 -*-

##sendMailForPrice
##源码 https://github.com/michaelliao/learn-python/blob/master/email/sendmail_multipart.py
##感谢 Michael Liao

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


from_addr = "13564945645@139.com"
password = "syy13564945645"
to_addr = "13564945645@139.com"
smtp_server = "smtp.139.com"


def _format_addr(s):
	name, addr = parseaddr(s)
	return formataddr(( \
		Header(name, 'utf-8').encode(), \
		addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def sendPicMail(pic):
	with open(pic, 'rb') as f:
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
	# server.set_debugl	evel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
