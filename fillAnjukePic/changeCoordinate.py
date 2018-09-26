#-*-coding:utf-8-*-

import os

def wCoor(pos):
	# print (os.getcwd())
	path = "F:\\python_code\\tempcode\\fillAnjukePic\\"
	##把坐标写入文件保存
	with open(path+"fillPic.py","r+",encoding="utf-8") as f:
		for i in f.readlines():
			if i.find('def signOutApp(nom_pos=') >= 0:
				# print (i.split("=")[1].split('):')[0])
				i = i.replace(i.split("=")[1].split('):')[0],pos)
				print(i)
			with open(path+"tempfillPic.py","a+",encoding="utf-8") as g:
				g.write(i)

	os.remove(path+"fillPic.py")
	os.rename(path+"tempfillPic.py",path+"fillPic.py")

def wCoorMI(pos):
	# print (os.getcwd())
	##把坐标写入文件保存
	with open("C:\\Users\\EACHPAL1\\Downloads\\codes\\code\\fillAnjukePic\\"+"fillPic.py","r+",encoding="utf-8") as f:
		for i in f.readlines():
			if i.find('def signOutAppMI(nom_pos=') >= 0:
				# print (i.split("=")[1].split('):')[0])
				i = i.replace(i.split("=")[1].split('):')[0],pos)
				print(i)
			with open("C:\\Users\\EACHPAL1\\Downloads\\codes\\code\\fillAnjukePic\\"+"tempfillPic.py","a+",encoding="utf-8") as g:
				g.write(i)

	os.remove("C:\\Users\\EACHPAL1\\Downloads\\codes\\code\\fillAnjukePic\\fillPic.py")
	os.rename("C:\\Users\\EACHPAL1\\Downloads\\codes\\code\\fillAnjukePic\\tempfillPic.py","C:\\Users\\EACHPAL1\\Downloads\\codes\\code\\fillAnjukePic\\fillPic.py")


# import linecache

# ##快速读取文件某一行
# text = linecache.getline('fillPic.py',202)
# print text