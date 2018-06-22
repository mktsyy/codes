#-*-coding:utf-8-*-
from openpyxl import load_workbook

wb = load_workbook(filename = '58发房.xlsx')
sheet_ranges = wb['6月22日']
print(sheet_ranges['I21'].value)
sheet_ranges['J21'].value = 100
print(sheet_ranges['J21'].value)
wb.save(filename = '58发房.xlsx')
