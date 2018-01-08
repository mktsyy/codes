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
# class testdll(Structure):  
#     _fields_=[('total',c_int),  
#              ('avg',c_double)]  

# pDll=WinDLL("test4.dll")

# ##其中sum是c的函数名称
# pDll.sum.restype=testdll 
# ARRAY = (c_int *13) #包含4个整数的数组类型
# a = ARRAY(0,1,2,3,4,5,6,7,8,9,0,11,12) #声明包含4个整数的数组，初值均为0     
# t=pDll.sum(a)  
# print t.total  
# print t.avg

##另外调用test5.dll

class testdll(Structure):  
    _fields_=[('Banker_wager',c_int),  
             ('Player_wager',c_int),
             ('Tie_wager',c_int),
             ('Pair_wager',c_int),
             ('DB_wager',c_int),
             ]  

pDll=WinDLL("test5.dll")

##其中sum是c的函数名称
pDll.Dec_bet.restype=testdll 
ARRAY = (c_int *14) #包含4个整数的数组类型
a = ARRAY(0,12,4,5,5,5,4,6,10,6,8,9,6,11)
# print len(a)
t=pDll.Dec_bet(a) 

print t.Banker_wager  
print t.Player_wager
print t.DB_wager
print t.Tie_wager
print t.Pair_wager
