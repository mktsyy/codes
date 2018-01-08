##Import_C
#-*-coding:utf-8-*-

from ctypes import *  

##调用C函数求和
# pDll=WinDLL("test.dll")
# print pDll.add(1,2)


##调用C的数组求和
# pDll=WinDLL("test3.dll")
# ARRAY = (c_int *13) #包含13个整数的数组类型
# a = ARRAY(0,1,2,3,4,5,6,7,8,9,0,11,12) #声明包含13个整数的数组   
# print pDll.sum(a)


##调用C函数结构

##针对c写出对应的结构类
class testdll(Structure):  
    _fields_=[('total',c_int),  
             ('avg',c_double)]  

pDll=WinDLL("test5.dll")

##其中sum是c的函数名称
pDll.Dec_bet.restype=testdll 
ARRAY = (c_int *14) #包含4个整数的数组类型
# a = ARRAY(0,1,2,3,4,5,6,7,8,9,0,11,12,13) #声明包含4个整数的数组，初值均为0     
a = ARRAY(0,1,2,3,3,3,3,3,3,3,3,3,3,3)
t=pDll.Dec_bet(a)  
print t.Banker_wager  
print Player_wager