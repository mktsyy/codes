#-*-coding:utf-8-*-

# 放到相片总文件夹目录，把相片从各自目录中取出
# 按照各自相片的创建时间，建立时间目录，然后把
# 相应照片放入对应目录
#完成时间2016年12月10日于家里

import os
import time
import shutil
import datetime

localdir = os.getcwd()
# print dir
for dst_dirpath, dst_dirnames, dst_filenames in os.walk(localdir,topdown=False):
	print dst_dirpath
	# print type(dst_dirpath)
# print dst_filenames
	# print type(dst_filenames)
	# print dst_filenames
	# print type(dst_dirnames)
	# print dst_dirnames
	# from IPython import embed#调用ipython进行调试
	# embed()
	
for i in dst_filenames:
	if i != "copyfiletodata.py":

		# from IPython import embed#调用ipython进行调试
		# embed()

		ad = os.path.getmtime(os.path.join(dst_dirpath,i))
		newdirstr = (datetime.datetime.fromtimestamp(ad)).strftime("%Y-%m-%d %H:%M:%S").split(" ")[0]
		newfilepath = os.path.join(localdir,newdirstr)
		# print newdirstr
			
		# print newfilepath
		newpath = os.path.join(newfilepath,i)
		# print newpath
		oldfilepath = os.path.join(dst_dirpath,i)
		# print oldfilepath
		

		if not os.path.isdir(newdirstr):
			os.mkdir(newdirstr)
			
		
		if not os.path.exists(newpath):
			# os.chdir(newfilepath)
			shutil.copy2(oldfilepath,newpath)
			# from IPython import embed#调用ipython进行调试
			# embed()
			os.remove(oldfilepath)
			# from IPython import embed#调用ipython进行调试
			# embed()
			continue
		else:
			if os.path.exists(oldfilepath):	
				os.remove(oldfilepath)
				# from IPython import embed#调用ipython进行调试
				# embed()
				continue

	

