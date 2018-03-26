# -*- coding: utf-8 -*-

import requests
import time

def showLast(url):
	r = requests.get(url)
	print ("EXX-last: " + eval(r.text)['ticker']['last'])
	print ("EXX-time: " + eval(r.text)['date'])
	# print eval(r.text)['ticker']['vol']

url = "https://api.exx.com/data/v1/ticker?currency=btc_usdt"

while True:
	showLast(url)
	time.sleep(1)