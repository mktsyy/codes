#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding: utf-8

'''
Provide user specific data and interact with gate.io
'''

from gateAPI import GateIO

## 填写 apiKey APISECRET
apiKey = ''
secretKey = ''
## address
btcAddress = 'your btc address'


## Provide constants

API_QUERY_URL = 'data.gateio.io'
API_TRADE_URL = 'api.gateio.io'

## Create a gate class instance

gate_query = GateIO(API_QUERY_URL, apiKey, secretKey)
gate_trade = GateIO(API_TRADE_URL, apiKey, secretKey)


# Trading Pairs
# print(gate_query.pairs())


## Below, use general methods that query the exchange

#  Market Info
# print(gate_query.marketinfo())

# Market Details
# print(gate_query.marketlist())

# Tickers
# print(gate_query.tickers())
# Depth
# print(gate_query.orderBooks())

# orders
# print(gate_query.openOrders())


## Below, use methods that make use of the users keys

# Ticker
print(gate_query.ticker('btc_usdt'))

from tkinter import *
import time
import when
import os
root = Tk()
##tk中独有的变量
var = StringVar()

root.title ("BTC")
##窗口置顶
root.wm_attributes('-topmost',1)
##label标签设置文本变量
Label(root, textvariable = var,font = 100).pack()

while True:
	time.sleep(1)
	try:
		# if gate_query.ticker('btc_usdt')['lowestAsk'] > 7700:
		# 	print ('gogogoogogogogogogo')
		# 	os.system("1.mp3")
		# var.set("BUY: "+str(gate_query.ticker('btc_usdt')['lowestAsk']) \
		# 	+"~~~ SELL: "+str(gate_query.ticker('btc_usdt')['highestBid'])+'~~~~'+str(when.now().strftime("%H:%M:%S")))
		# root.update()

		print ("比原链_BUY: " +str(gate_query.ticker('btm_usdt')['lowestAsk']) \
			+"~~~~SELL: "+str(gate_query.ticker('btm_usdt')['highestBid'])+'~~~~'+str(when.now().strftime("%H:%M:%S")))
	except:
		pass

# Market depth of pair
# print(gate_query.orderBook('btc_usdt'))

# Trade History
# print(gate_query.tradeHistory('btc_usdt'))

# Get account fund balances
# print(gate_trade.balances())

# get new address
# print(gate_trade.depositAddres('btc'))

# get deposit withdrawal history
# print(gate_trade.depositsWithdrawals('1469092370', '1569092370'))

# Place order sell
# print(gate_trade.buy('etc_btc', '0.001', '123'))

# Place order sell
# print(gate_trade.sell('etc_btc', '0.001', '123'))

# Cancel order
# print(gate_trade.cancelOrder('267040896', 'etc_btc'))

# Cancel all orders
# print(gate_trade.cancelAllOrders('0', 'etc_btc'))

# Get order status
# print(gate_trade.getOrder('267040896', 'eth_btc'))

# Get my last 24h trades
# print(gate_trade.mytradeHistory('etc_btc', '267040896'))

# withdraw
# print(gate_trade.withdraw('btc', '88', btcAddress))