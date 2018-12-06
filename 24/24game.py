# encoding: utf-8
'''
@author: GaryLee
@software: PyCharm
@file: 24game.py
@time: 2018/9/26 22:50
'''
import itertools
import random
##加入游戏UI
from tkinter import *
from tkinter import ttk
import os
import time
import sys

cardNum = []    # 存放随机牌组
listSet = []    # 存放随机牌组对
cardGroup = ()  # 调用牌组
symbols = ["+","-","*","/"]  #存放运算符
cardOne = 0 ; cardTwo = 0 ; cardThr = 0 ;cardFor = 0    # 存放卡牌信息
resultOne = 0 ; resultTwo = 0 ; resultThr = 0   # 存放运算计算结果
cardValue = []  # 保存结果打印信息
cardResult = []   #存放运算结果

# 发牌器
def cardFun():
	for i in range(4):
		cardNum.append(int(random.random() * 100 % 13) + 1)
	# cardNum = [8,9,6,10]
	listSet = list(set(itertools.permutations(cardNum, 4)))
	return listSet         # 存放A(4,4)种排列方式的列表

# 计算方法
cardList = cardFun()     #将生成的四张牌所有排列顺序放入cardList中
def cardCompute():
	for i in range(len(cardList)):
		cardGroup = cardList[i]
		cardOne = cardGroup[0]
		cardTwo = cardGroup[1]
		cardThr = cardGroup[2]
		cardFor = cardGroup[3]
		flag = False
		# 下面的循环运算体系会有数学上逻辑上的报错，所以用try检测
		try:
			for s1 in symbols:
				resultOne = 0
				if s1 == "+":
					resultOne = cardOne + cardTwo
				elif s1 == "-":
					resultOne = cardOne - cardTwo
				elif s1 == "*":
					resultOne = cardOne * cardTwo
				elif s1 == "/":
					resultOne = cardOne / cardTwo
				for s2 in symbols:
					resultTwo = 0
					if s2 == "+":
						resultTwo = resultOne + cardThr
					elif s2 == "-":
						resultTwo = resultOne - cardThr
					elif s2 == "*":
						resultTwo = resultOne * cardThr
					elif s2 == "/":
						resultTwo = resultOne / cardThr
					for s3 in symbols:
						resultThr =0 ; resultelse = 0
						if s3 == "+":
							resultThr = resultTwo + cardFor
							resultelse = cardThr + cardFor
						elif s3 == "-":
							resultThr = resultTwo - cardFor
							resultelse = cardThr - cardFor
						elif s3 == "*":
							resultThr = resultTwo * cardFor
							resultelse = cardThr * cardFor
						elif s3 == "/":
							resultThr = resultTwo / cardFor
							resultelse = cardThr / cardFor

						# 判断最终结果是否为24
						if resultThr == 24:
							cardValue.append("((%s %s %s) %s %s ) %s %s = 24" % (cardOne,s1,cardTwo,s2,cardThr,s3,cardFor))
							flag = True
						# 括号与括号的运算
						elif resultThr != 24 and 24 % resultOne == 0:
							for s4 in symbols:
								resultThr = 0
								if s4 == "+":
									resultThr = resultOne + resultelse
								elif s4 == "-":
									resultThr = resultOne - resultelse
								elif s4 == "*":
									resultThr = resultOne * resultelse
								elif s4 == "/":
									resultThr = resultOne / resultelse
								if resultThr == 24:
									cardValue.append("(%s %s %s) %s (%s %s %s) = 24" % (cardOne,s1,cardTwo,s4,cardThr,s3,cardFor))
									flag = True
								if flag:
									break
					# 如果得到结果，就退出3次运算的循环
						if flag:
							break
					if flag:
						break
				if flag:
					break
		except ZeroDivisionError:
			pass

	cardResult = set(cardValue)
	# print ((cardResult)[0])
	return cardResult

##界面类

class App:
	def caculation(self, content, name):
		# kk = "self.e%s.get()" % str(k)
		# print (kk)
		# if eval(kk):
		#   print (eval(kk))
		# pass
		# print ("ok")
		# while True:
		#   self.label = Label(frame1, textvariable = g)
		#   self.label.grid(row = 2 +g, column = 2)
		# if self.midy.get():
		# print (content,name)
		# print (type(name))
		#如果拿到数据，再进行数据填充
		if content:
			##拿到算式错误不报错直接跳过
			try:
				self.sumAll.set(int(eval(content)))
			except:
				pass
		# if content:
		#   if name == ".!frame.!entry":
		#       self.sumAll0.set(eval(content))
		#   else:
		#       k = "sumAll" + str(int(name.split("entry")[1]) - 1)
		#       self.k.set(eval(content))
		##返回True保证每次都检查算式
		return True
	
	
	# def show(self, event):
	#   ##原来用paneswindow方法来展示，现在换Toplevel方法来展示
	#   # print (self.button["text"] == "关闭")
	#   # print (self.button["state"])

	#   ##拿到的可以计算的算法集
	#   global com1
	#   # global flag
	#   ##PanedWindow 见https://blog.csdn.net/m0_37264397/article/details/79101311
	#   # if isinstance(com1,set):
	#   if self.button["text"] == "查看":
	#       # print (com1)
	#       ##算法set排列
	#       for g,i in enumerate(com1):
	#           ##Label变量准备
	#           com2 = StringVar()
	#           com2.set(str(g+1) + " ..." + i)
	#           # self.label = Label(textvariable = com1,font=("Arial", 20))
	#           # self.label.pack()
	#           ##该用panes来添加窗口
	#           ##panes窗口内容加入self.ws列表
	#           ##关于表格内再分，前面想复杂了，其实只要用grid来划分就可以了(加了grid有问题了，不能关闭了，待寻问题)
	#           if g % 2 == 0:
	#               vRow = int(g/2 + 1)
	#               self.ws.append(Label(self.panes, textvariable = com2,font=("Arial", 12)))
	#           else:
	#               vRow = int(g // 2 + 1)
	#               self.ws.append(Label(self.panes, textvariable = com2,font=("Arial", 12)))
	#           # flag = False
	#           ##按钮提示内容变换
	#           self.button["text"] = "关闭"
	#           # print (self.button["text"])
	#       # print (ws)
	#       # print (self.ws)
	#       ##panes窗口内容填充
	#       for w in self.ws:
	#           self.panes.add(w)

	#   ##按钮文字为“关闭”
	#   else:
	#       # flag = True
	#       # print (self.ws)
	#       ##按钮提示内容变换
	#       self.button["text"] = "查看"
	#       ##panes窗口内容移除
	#       for w in self.ws:
	#           self.panes.remove(w)
	#       ##清空列表，以免算数表达式增长
	#       self.ws = []
	#       # print (self.ws)
	#       # self.master.update()
	#       # self.hide()

	#   # elif isinstance(com1,StringVar):
	#   #   ##方法展示
	#   #   self.label = Label(textvariable = "",font=("Arial", 20))
	#   #   self.label.pack()
	#   #   # print ("here")
	#   #   # self.button["state"]== "disable"
	#   #   com1 = StringVar()

	def show(self,event):
		global com1
		answer = Toplevel()
		##前面参数为窗口大小是一个参数x参数的格式，后面+号和+号的是位置参数
		##从https://blog.csdn.net/sm9sun/article/details/53743116得灵感，
		##窗口自适应参数可以如下写
		answer.geometry('+1000+300')
		# answer.resizable(0,0)

		##打印窗口的宽度
		answer.update()
		# answer.iconposition(x = 1500, y = 200)
		# print (answer.iconposition())
		print (answer.winfo_width())

		answer.title(u"答案")
		# handler = lambda: self.onCloseAnswer(answer)
		# btn = ttk.Button(answer, text="Close", command=handler)
		# btn.pack()
		for i,g in enumerate(com1):
			sort22 = StringVar()
			# print (g)
			sort22.set(g)
			label = Label(answer, textvariable = sort22, font=("Arial", 12))
			# if i % 2 == 0:
				# label.grid(row = i + 1, column = 2,columnspan = 2)
				# label.pack()
			# else:
				# label.grid(row = i , column = 2,columnspan = 2)
			label.pack()


	def onCloseAnswer(self):
		pass

	##此方法废弃
	def hide(self):
		global flag

		if flag:
			##主窗口延迟64毫秒进行函数内循环
			self.master.after(64, self.hide)

	def reboot(self, event):
		##重启程序
		python = sys.executable
		os.execl(python, python, * sys.argv)

	def on_closing(self):
		##gui关闭时调用此方法
		try:
			os.system("taskkill /F /IM osk.exe")
		except:
			pass
		root.destroy()

	def destroy(self):
		##gui关闭时不调用此方法(废弃)
		os.system("taskkill /F /IM osk.exe")
			

	def __init__(self,master,cardnum,kind,com):
		##加入样式
		style = ttk.Style()
		# print (style.theme_names())
		style.configure('BW.TLabel', foreground="black", background="white")

		##函数包装一下，准备获取值
		test_cmd = master.register(self.caculation)

		self.master = master

		frame1 = Frame(master)
		frame1.pack()
		##随机生成的卡牌数
		self.label = ttk.Label(frame1,textvariable = cardnum,font=("Arial", 20), style='BW.TLabel')
		self.label.grid(row = 1, column = 1,columnspan = 2)
		##占位
		# self.label = Label(frame1,text = "-------------",font=("Arial", 20))
		# self.label.grid(row = 1, column = 2)
		##显示卡牌总共算法
		self.label = ttk.Label(frame1,textvariable = kind,font=("Arial", 20), style='BW.TLabel')
		self.label.grid(row = 1, column = 3, columnspan = 3)

		##打印所有算法
		# print (type(com))
		global com1
		com1 = com
		for g,i in enumerate(com1):
			# print (type(i))
			# com = StringVar()
			# com.set(i)
			##方法变量
			sorts = StringVar()
			sorts.set("方法"+str(g+1)+".")
			##填入算法
			self.midy = "self." + "e%s" % str(g)
			# print (midy)
			value = StringVar()
			##验证方法加入获取输入款值和组件名称
			self.midy = Entry(frame1,  font=("Arial", 15), textvariable = value, \
				validate='focus',validatecommand=(test_cmd, '%P', '%W') )
			if g % 2 == 0:
				##方法排版
				vRow = int(g/2 + 2)
				self.label = Label(frame1, textvariable = sorts, font=("Arial", 12), ).grid(row = vRow, column = 1)             
				self.midy.grid(row =vRow, column = 2)
			else:
				vRow = int(g // 2 + 2)
				self.label = Label(frame1, textvariable = sorts, font=("Arial", 12), ).grid(row = vRow, column = 3)             
				self.midy.grid(row =vRow, column = 4)

			# print (midy)
			##判断正确或错误
			# midx = "self." + "button%s" % str(g)
			# print (midx)
			# midx = Button(frame1, text = "检查")
			# midx.grid(row = 2 + g, column = 2)

			##用label块来显示结果
			
			# self.caculation(frame1, value)
			# self.sumAll = "self." + "sumAll%s" % str(g)
			# print (self.sumAll)
			self.sumAll = StringVar()
			self.label = "self." + "label%s" % str(g)
			# print (self.label)
			self.label = Label(frame1, textvariable = self.sumAll, font=("Arial", 30),  fg = "red")
			# value.set(midy.get())
		self.label.grid(row = 5 , column = 5)
			##方法展示
			# self.label = Label(frame1,textvariable = com,font=("Arial", 20))
			# self.label.grid(row = 2 + g , column = 3)
			##检查结果是否是24
			# midx.bind("<ButtonRelease-1>",lambda midy:print(midy))\


		##算法显示部分，还未搞定
		# def show(frame1, com):
		#   if self.button["text"] == "关闭":
		#       ##方法展示
		#       self.label = Label(frame1,textvariable = "",font=("Arial", 20))
		#       self.label.grid(row = 2  , column = 3)
		#       self.button["text"] == "查看"
		#   else:
		#       for g,i in enumerate(com):
		#           com = StringVar()
		#           com.set(i)
		#           self.label = Label(frame1,textvariable = com,font=("Arial", 20))
		#           self.label.grid(row = 2 + g , column = 3)
		#       self.button["text"] == "关闭"

		self.button = ttk.Button(frame1, text = "查看", style='BW.TLabel')
		# self.button["state"]== "disable"
		self.button.grid(row = 2, column = 5)
		self.button.bind("<ButtonRelease-1>",self.show)
		# master.update()

		##重启按钮
		self.button99 = ttk.Button(frame1, text = "再来一组", style="BW.TLabel")
		# self.button["state"]== "disable"
		self.button99.grid(row = 4, column = 5)
		self.button99.bind("<ButtonRelease-1>",self.reboot)


		##为panes准备的集合(类自变量和普通变量有区别？<--错误认识，不是所说的这种问题)
		##布局一定按照从上到下，从左到右的来进行，不然会覆盖
		##panes窗口列表
		# self.ws = []
		##panes窗口准备
		# self.panes = PanedWindow(orient=VERTICAL, width = 40 ,showhandle=True,sashrelief=SUNKEN, relief = RAISED)
		# self.panes.pack(fill = BOTH,expand = 1)
		# self.panesH = PanedWindow(orient=HORIZONTAL, width = 40 ,showhandle=True)
		# self.panesH.pack(fill = BOTH,expand = 1)

		##滚动卷轴(panes没有yview参数。。。。。)
		# scrollbar = Scrollbar(master)
		# scrollbar.pack( side = RIGHT, fill = Y )
		# scrollbar.config( command = self.panes.yview )

		##gui关闭时调用的方法
		self.master.protocol("WM_DELETE_WINDOW", self.on_closing)


# 执行主体
if __name__ == "__main__":
	Compute = cardCompute()
	if len(Compute) == 0:
		##重启程序
		python = sys.executable
		os.execl(python, python, * sys.argv)

	print("这组卡牌共有 %s 种算法" % (len(Compute)))
	print("---" * 10)
	# for i in Compute:
	#     print(i)

	##界面主题
	root = Tk()
	root.title("24点游戏")
	# root.wm_attributes('-topmost',1)
	##生成的卡牌数
	cardnum = StringVar()
	##总共有多少种算法
	kind = StringVar()
	##显示所有算法
	# com = StringVar()
	##界面显示生成的数字
	cardnum.set(u"你手上的卡牌为：%s %s %s %s" % (cardList[0][0],cardList[0][1],cardList[0][2],cardList[0][3]))
	##界面显示算法数
	kind.set(u"-----共有 %s 种算法" % (len(Compute)))
	##所有算法传入界面显示
	# com.set(Compute)
	display = App(root,cardnum,kind,Compute)

	##q启动屏幕键盘
	os.system("osk.exe")

	root.mainloop()


