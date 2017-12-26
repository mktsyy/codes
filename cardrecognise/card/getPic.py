#getpic
#-*-coding:utf-8-*-


import rightcard
import leftcard
import middlecard
import middlecardbanker
import rightcardbanker
import leftcardbanker
import time

while True:
	# pass
	time.sleep(0.2)
	middlecard.main()
	rightcard.main()
	leftcard.main()
	middlecardbanker.main()
	rightcardbanker.main()
	leftcardbanker.main()