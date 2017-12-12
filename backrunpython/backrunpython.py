# -*- coding: utf-8 -*-

# A sample demonstrating the smallest possible service written in Python.
##今天想用#twisted#写个脚本顺便用twistd启动后在后台运行，后发怎么都不行，
# 网上查了下应该是windows不支持，linux下是可以通过 twistd -oy XX.py 放到后台运行的（我还没试）。
# 然后只能用pywin32的一个模板写了一个server跑在xp上，就可以做到在后台运行了。附上模板代码图，我也网上搜到的。

##启动的方法就是直接在cmd下，脚本名.py install ，
##然后去windows 的服务下就可以看到The smallest possible Python Service 这个服务，你可以启动，停止，还可以设置成开机自动启动。

import win32serviceutil
import win32service
import win32event
import time
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

class SmallestPythonService(win32serviceutil.ServiceFramework):
    _svc_name_ = "SmallestPythonService"
    _svc_display_name_ = "The smallest possible Python Service"
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        # Create an event which we will use to wait on.
        # The "service stop" request will set this event.
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    ##增加定时发邮件
    def format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    

   

    def SvcStop(self):
        # Before we do anything, tell the SCM we are starting the stop process.
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        # And set my event.
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        #what to do#
        ##增加定时发邮件
        # from_addr = "13564945645@139.com"
        # password = ""
        # to_addr = "13564945645@139.com"
        # smtp_server = "smtp.139.com"

        # msg = MIMEMultipart()
        # msg['From'] = self.format_addr('桌面截图')
        # msg['To'] = self.format_addr('管理员')
        # msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

        # add MIMEText:
        # msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))


        #截图
        # im = ImageGrab.grab() 
        # im.save(os.getcwd()+"\\screenshot.png")#保存图片 

        # # add file:
        # with open('screenshot.png', 'rb') as f:
        #     mime = MIMEBase('image', 'png', filename='screenshot.png')
        #     mime.add_header('Content-Disposition', 'attachment', filename='screenshot.png')
        #     mime.add_header('Content-ID', '<0>')
        #     mime.add_header('X-Attachment-Id', '0')
        #     mime.set_payload(f.read())
        #     encoders.encode_base64(mime)
        #     msg.attach(mime)

        # while True:
        #     server = smtplib.SMTP(smtp_server, 25)
        #     server.set_debuglevel(1)
        #     server.login(from_addr, password)
        #     server.sendmail(from_addr, [to_addr], msg.as_string())
        #     server.quit()
        #     time.sleep(5)

        #调用shell命令
        os.system('python D:\\littleapp\\sendmail\\sendmail.py')

        win32event.WaitForSingleObject(self.hWaitStop, win32event.INFINITE)



if __name__=='__main__':
    win32serviceutil.HandleCommandLine(SmallestPythonService) 