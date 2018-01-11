##cardNum
#-*-coding:utf-8-*-


cardAllNum = []
k = 0
print cardAllNum.count('A')
basicCard =['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] 
for i in basicCard:
	while k < 32:
		cardAllNum.append(i)
		k = k + 1
	k = 0

print cardAllNum.count('A')
print cardAllNum.count('2')
print cardAllNum.count('10')