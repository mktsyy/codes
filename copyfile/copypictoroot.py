#-*-coding:utf-8-*-

##从目录下各文件夹拿出图片文件放入根目录

import os
import time
import shutil
import datetime

localdir = os.getcwd()
# print dir
for dst_dirpath, dst_dirnames, dst_filenames in os.walk(localdir,topdown=False):
	for i in dst_filenames:
		if i != "copypictoroot.py":
			oldfilepath = os.path.join(dst_dirpath,i)
			newfilepath = os.path.join(localdir,i)
			shutil.copy2(oldfilepath,newfilepath)
			os.remove(oldfilepath)
			continue
