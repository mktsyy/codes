# -*- coding: utf-8 -*-

import os

def saveIMI(num):
	print (num)
	path = "C:\\Users\\EACHPAL1\\Downloads\\codes\\code\\fillAnjukePic\\"
	##把I写入文件保存
	with open(path+"fillMobilApp_NJWH.py","r+",encoding="utf-8") as f:
		for n,i in enumerate(f.readlines()):
			if i.find('I =') >= 0:
				if n == 124:
					i = i.replace(i.split("=")[1],str(num)+"\n")
					print(i)
			with open(path+"tempfillMobilApp_NJWH.py","a+",encoding="utf-8") as g:
				g.write(i)

	os.remove(path+"fillMobilApp_NJWH.py")
	os.rename(path+"tempfillMobilApp_NJWH.py",path+"fillMobilApp_NJWH.py")

def saveI(num):
	path = "F:\\python_code\\tempcode\\fillAnjukePic\\"
	##把I写入文件保存
	with open(path+"fillMobilApp_NJWH.py","r+",encoding="utf-8") as f:
		for n,i in enumerate(f.readlines()):
			if i.find('I =') >= 0:
				if n == 124:
					i = i.replace(i.split("=")[1],str(num)+"\n")
					print(i)
			with open(path+"tempfillMobilApp_NJWH.py","a+",encoding="utf-8") as g:
				g.write(i)

	os.remove(path+"fillMobilApp_NJWH.py")
	os.rename(path+"tempfillMobilApp_NJWH.py",path+"fillMobilApp_NJWH.py")