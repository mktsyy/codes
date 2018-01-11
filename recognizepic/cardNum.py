##cardNum
#-*-coding:utf-8-*-


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
