#-*-coding:utf-8-*-

from fillPic import HZadmin,HZadminSolo,HZadminPublic,newPublic
from tkinter import *
from tkinter import ttk
import os
import time

class App:

	def buttonListener1(self,event):
		# HZadmin()
		##打印绑定的账号
		# print(self.button1.get())
		pass

	def buttonListener2(self,event):
		##打开右侧console，粘帖代码，并选择所有本页房源
		HZadminSolo()
		# print(self.button1.get())
		##点击发布并选择相应账号进行发布
		newPublic(self.button1.get())

	def buttonListener3(self,event):
		HZadminPublic()

	def buttonListener4(self,event):

		##获取链接，准备把链接转换成多个页面
		var = self.e.get()

		##没有清除文本框，待查
		# self.e.insert(0, END)

		print (var)
		# print (var.split("p/")[1].split('/region')[0])
		## print (var.split("p/")[0]+ "p/%s"  + '/region'% "888")

		##生成html文件并自动默认浏览器打开
		with open("cityurl.html",'w+',encoding='utf-8') as g:
			htmlhead='''
			<!DOCTYPE html>
			<html lang="en">
			<head>
				<meta charset="UTF-8">
				<title>Document</title>
				<script type="text/javascript">
			function openurl(num){
				// alert("here")
				i = 3
				do{
					document.getElementsByTagName("a")[num-i].click();
					document.getElementsByTagName("a")[num-i].style.color="#ff0000";
					i++;
				} while(i<13)
			}
				</script>
			</head>
			<body>
			'''

			
			g.write(htmlhead)

			##生成页码数
			for i in range(2,35):

				url = var.split("p/")[0] + "p/%s"  % str(i)
				try:
					newurl = '<A HREF="%s" target="_blank" >第%s页</A>\n' % (url + '/region' + var.split("p/")[1].split('/region')[1],str(i))
				except:
					newurl = '<A HREF="%s" target="_blank" >第%s页</A>\n' % (url+ '/moneyMin' + var.split('/moneyMin')[1],str(i))
				print (newurl)

				if (i-2) % 10 == 0:
					g.write('<button onclick="openurl(%s)">打开</button><br>\n' % str(i))

				g.write(newurl)

			# import os
			# print (os.getcwd())

			htmlend='''
			</body>
			</html>
			'''
			g.write(htmlend)

		os.system("cityurl.html")


	def __init__(self,master):

		##加入输入框准备后端获取链接，进行改造
		self.e = Entry(master)
		self.e.pack()
		
		##用框架，grid方法来划分
		frame1 = Frame(master)
		frame1.pack()  #看下面的解释（包管理器）
		self.label = Label(frame1,text = "选择：")
		self.label.grid(row = 1, column = 1)

		##不再需要翻页方法
		# self.button1 = Button(frame1,width=15,text='操作')
		# self.button1.grid(row = 1, column = 2)

		##重新定义为选择框，选择发布账号
		number = StringVar()
		self.button1 = ttk.Combobox(frame1,width=15,text=number)
		self.button1['values'] = ("徐汇:13795419927", "长宁:18674586768", "浦东:13296760994", \
								 "浦东:嗨住全国12", "杨浦:嗨住全国11","普陀:18202158542", \
								 "闵行:13641026605","闵行:嗨住全国13","闸北:18768113824", \
								  "宝山:15136289152","宝山:嗨住全国15","嘉定:15026518260", \
								  "嘉定:嗨住全国16","松江:13810794175","松江:嗨住全国14", \
								  "青浦:18670107293","朝阳&丰台:嗨住2017","海淀&大兴:嗨住2018", \
								  "郑州:上海高度公司","龙岗1", "南山1", "福田1", "宝安1", "龙华", \
								  "罗湖", "龙岗", "南山", "福田", "宝安",
								   ) 
		self.button1.grid(row = 1, column = 2)

		self.button2 = Button(width=25,text='发布')
		self.button2.pack()
		# self.button3 = Button(width=25,text='发布')
		# self.button3.pack()
		##获取输入框内容按钮
		self.button4 = Button(width=25,text='链接转换')
		self.button4.pack()

		##焦点为button1
		self.button1.focus_set()

		self.button1.bind("<<ComboboxSelected>>",self.buttonListener1)
		self.button2.bind("<ButtonRelease-1>",self.buttonListener2)
		# self.button3.bind("<ButtonRelease-1>",self.buttonListener3)
		self.button4.bind("<ButtonRelease-1>",self.buttonListener4)

root = Tk()
root.title("嗨住后台")
root.wm_attributes('-topmost',1)
display = App(root)
root.mainloop()