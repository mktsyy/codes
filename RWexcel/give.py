#-*-coding:utf-8-*-
import xlrd#导入xlrd模块
import time
import os
from xlutils.copy import copy #模块名xlutils,此模块可以编辑已经存在的excel文件

bk = xlrd.open_workbook('wacai.xls')
one= bk.sheet_names()[3]#读取表格的第四个sheet
sh = bk.sheet_by_name(one)
# ufo_color = sh.cell_value(1,1)#ufo_color
i=1
fileName = 'miniend.xls'
oldWb = xlrd.open_workbook(fileName,formatting_info=True)
newWb = copy(oldWb)#复制一个备份，不在原表格上进行操作
newWs = newWb.get_sheet(0)
while i < 277:#这里的行数是根据nrows = sh.nrows得出的
	ufo_color = sh.cell_value(i,3)#读取ufo的颜色
	dataa = sh.cell_value(i,1)#读取日期
	ufo_user = sh.cell_value(i,2)#读取人员
	ufo_num = sh.cell_value(i,4)#读取数量
	if sh.cell_value(i,0) == u"借出":	#判断，因为读取出的也是unicode，所以这里也用一样的来进行配置
		
		if ufo_color == u'ufo黑':
			newWs.write(i+805,2,ufo_num)#写入的位置需要手动定位一下
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'手表':
			newWs.write(i+805,6,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'ufo红':
			newWs.write(i+805,5,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'SMW蓝':
			newWs.write(i+805,8,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'ufo橙':
			newWs.write(i+805,4,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'SMW黑':
			newWs.write(i+805,7,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'ufo黄':
			newWs.write(i+805,3,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'SMW金':
			newWs.write(i+805,9,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == 'SK':
			newWs.write(i+805,10,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)


	else:
		if ufo_color == u'ufo黑':
			newWs.write(i+805,11,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'手表':
			newWs.write(i+805,15,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'ufo红':
			newWs.write(i+805,14,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'SMW蓝':
			newWs.write(i+805,17,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'ufo橙':
			newWs.write(i+805,13,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'SMW黑':
			newWs.write(i+805,16,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'ufo黄':
			newWs.write(i+805,12,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == u'SMW金':
			newWs.write(i+805,18,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)
		elif ufo_color == 'SK':
			newWs.write(i+805,19,ufo_num)
			newWs.write(i+805,1,ufo_user)
			newWs.write(i+805,0,dataa)

			
	newWb.save('mini5.xls')#保存
	i+=1#循环