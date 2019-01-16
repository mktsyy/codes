#-*-coding:utf-8-*-
from openpyxl import load_workbook##此模块对xls不支持，换xlrd模块
import xlrd#导入xlrd模块

##装载表格
# wb = load_workbook(filename = '2019-01-05.xlsx')
# sheet_ranges = wb['Page1']
# print sheet_ranges["B1"].value

bk = xlrd.open_workbook('2019-01-05.xls')
one= bk.sheet_names()[0]#读取表格的第一个sheet
sh = bk.sheet_by_name(one)
# print sh.cell_value(1,0)
# print range(10)
# print sh.nrows
# print sh.ncols
k = 0
a = 0
while k < 10:
	for i in range(sh.ncols):
		print sh.cell_value(k,i) 
	k = k + 1