# -*- coding: utf-8 -*-
import requests
import urllib2


url = "http://m.hizhu.com/Home/House/getsearchekey.html?keyword=%s&city_code=001010001" % urllib2.quote("佳和园 ")
# print url
r = requests.get(url).text

getdata =  eval(r)['data'][len(eval(r)['data'])-1]
print len(eval(r)['data'])
print getdata
# 
geturl ='''http://m.hizhu.com/nanjing/rentlist.html?keyself=2&keyword=%s&type_no=0&search_id=%s&result_no=%s&lat=&lng=&key=%s&city_code=001010001&city_name=nanjing#&logicSort=2''' % (getdata["estate_name"],getdata["id"],getdata["result_no"],getdata["estate_name"])
print geturl