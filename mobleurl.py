# -*- coding: utf-8 -*-
# 
import requests
import urllib2
import os
import time

llll=1
with open("party.txt",'r') as f:

	with open("newmoble.html",'a+') as g:
		htmlhead='''
		<!DOCTYPE html>
		<html lang="en">
		<head>
			<meta charset="UTF-8">
			<title>Document</title>
			<script type="text/javascript">
		function openurl(num){
			// alert("here")
			i = 1
			do{
				document.getElementsByTagName("a")[num-i].click();
				document.getElementsByTagName("a")[num-i].style.color="#ff0000";
				i++;
			} while(i<11)
		}
			</script>
		</head>
		<body>
		'''

		
		g.write(htmlhead)

		for k in f.readlines():
			time.sleep(10)
			url = "http://m.hizhu.com/Home/House/getsearchekey.html?keyword=%s&city_code=001010001" % k
			print url
			try:
				r = requests.get(url).text

				getdata =  eval(r)['data'][len(eval(r)['data'])-1]
				print len(eval(r)['data'])
				# 
				geturl ='''http://m.hizhu.com/nanjing/rentlist.html?keyself=2&keyword=%s&type_no=0&search_id=%s&result_no=%s&lat=&lng=&key=%s&city_code=001010001&city_name=nanjing#&logicSort=2''' % (k,getdata["id"],getdata["result_no"],k)
				print geturl
				
				
				a = str(llll)+'''.<A HREF="%s" target="_blank" >%s</A>''' % (geturl,k)
				
				if llll % 10 == 0:
					button = '<button onclick="openurl(%s)">打开</button>' % str(llll)
					g.write(a+button+"<br>"+"\n")	
				# elif llll % 10 == 0:
				# 	g.write(i+"\n"+"<br>")

				else:
					g.write(a+"\n")
					print str(llll)+"done!"
			except:
					print "wrong.........................."
					print llll

			llll+=1
	


		htmlend='''
		</body>
		</html>
		'''
		g.write(htmlend)