##cardNum
#-*-coding:utf-8-*-
##8付牌生成列表


cardAllNum = []
k = 0
print cardAllNum.count('A')
basicCard = ['0','A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
for i in basicCard:
	while k < 32:
		cardAllNum.append(i)
		k = k + 1
	k = 0

print cardAllNum.count('A')
print cardAllNum.count('2')
print cardAllNum.count('10')
cardAllNum.remove('A')
print cardAllNum.count('A')

print [
'0'+':'+str(cardAllNum.count('0')), 
'A'+':'+str(cardAllNum.count('A')), 
'2'+':'+str(cardAllNum.count('2')), 
'3'+':'+str(cardAllNum.count('3')), 
'4'+':'+str(cardAllNum.count('4')),
'5'+':'+str(cardAllNum.count('5')), 
'6'+':'+str(cardAllNum.count('6')), 
'7'+':'+str(cardAllNum.count('7')), 
'8'+':'+str(cardAllNum.count('8')), 
'9'+':'+str(cardAllNum.count('9')), 
'10'+':'+str(cardAllNum.count('10')), 
'J'+':'+str(cardAllNum.count('J')), 
'Q'+':'+str(cardAllNum.count('Q')), 
'K'+':'+str(cardAllNum.count('K'))
] 


##以下为测试如何通过字典调用函数
# def Banker_wager(num):
# 	print num
# def Player_wager(num):
# 	print num
# def DB_wager(num):
# 	print num
# def Tie_wager(num):
# 	print num
# def Pair_wager(num):
# 	print num	
# def gogogo(name,num):
# 	if name == "Banker_wager":
# 		Banker_wager(num)
# 	elif name == "Player_wager":
# 		Player_wager(num)
# 	elif name == "DB_wager":
# 		DB_wager(num)
# 	elif name == "Tie_wager":
# 		Tie_wager(num)
# 	elif name == "Pair_wager":
# 		Pair_wager(num)

# class ttt():

# 	Banker_wager = 1
# 	Player_wager = 2
# 	Pair_wager = 3
# 	DB_wager = 4
# 	Tie_wager = 5

# t = ttt()
# import time

# wagerlist = {"t.Banker_wager":t.Banker_wager, "t.Player_wager":t.Player_wager, "t.DB_wager":t.DB_wager, "t.Tie_wager":t.Tie_wager, "t.Pair_wager":t.Pair_wager}
# for wagerName,wagerValue in wagerlist.items():
# 	if wagerValue > 0:
# 		# if wagerValue == 1:
# 		# 	# oneCoin()
# 		# 	time.sleep(0.1)
			
# 		# 	gogogo(wagerName.split('.')[1],2)
# 		# elif wagerValue == 3:
# 		# 	# oneCoin()
# 		# 	time.sleep(0.1)
# 		# 	print wagerName.split('.')[1]
# 		# 	# str(wagerName.split('.')[1])(3)
# 		# elif wagerValue == 5:
# 		# 	# fiveCoin()
# 		# 	time.sleep(0.1)
# 		# 	print wagerName.split('.')[1]
# 		# 	# str(wagerName.split('.')[1])(1)
# 		# elif wagerValue == 7:
# 		# 	# oneCoin()
# 		# 	time.sleep(0.1)
# 		# 	print wagerName.split('.')[1]
# 		# 	# str(wagerName.split('.')[1])(2)
# 		# 	# fiveCoin()
		
# 		# 	print wagerName.split('.')[1]	
# 		# 	# str(wagerName.split('.')[1])(1)
# 		# elif wagerValue == 10:
# 		# 	# fiveCoin()
# 		# 	time.sleep(0.1)
# 		# 	print wagerName.split('.')[1]
# 		# 	# str(wagerName.split('.')[1])(2)

# 		gogogo (wagerName.split('.')[1],wagerValue)

# Banker_wager=1
# Player_wager=2
# DB_wager=3
# Tie_wager=4
# Pair_wager=5
# wagerlist = [Banker_wager,Player_wager,DB_wager,Tie_wager,Pair_wager]
# wagerName = ["Banker_wager","Player_wager","DB_wager","Tie_wager","Pair_wager"]
# gg = 0
# for iiii in wagerlist:
# 	if iiii > 0:
# 		for kk in wagerName:
# 			if wagerName[gg] == kk:
# 				gg = gg + 1
