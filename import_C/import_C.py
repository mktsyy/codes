##Import_C
#-*-coding:utf-8-*-

from ctypes import *  

##调用C函数求和
# pDll=WinDLL("test.dll")
# print pDll.add(1,2)

##调用C的数组求和
# pDll=WinDLL("test3.dll")
# ARRAY = (c_int *13) #包含4个整数的数组类型
# a = ARRAY(0,1,2,3,4,5,6,7,8,9,0,11,12) #声明包含4个整数的数组，初值均为0      
# print pDll.sum(a)

##调用C函数结构
class testdll(Structure):  
    _fields_=[('total',c_int),  
             ('avg',c_double)]  
t=testdll()  
t.total=10  
t.avg=0.2 

pDll=WinDLL("test4.dll")
pDll.sum.restype=testdll 
ARRAY = (c_int *13) #包含4个整数的数组类型
a = ARRAY(0,1,2,3,4,5,6,7,8,9,0,11,12) #声明包含4个整数的数组，初值均为0     
t=pDll.sum(a)  
print t.total  
print t.avg