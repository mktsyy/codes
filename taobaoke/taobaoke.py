# -*- coding: utf-8 -*-
import top.api
import json

##淘宝客商品查询
# req=top.api.TbkItemGetRequest()
# req.set_app_info(top.appinfo("25527845","a17bff452a120a8e4fd3ea8e4299fb14"))

# req.fields="num_iid,title,pict_url,small_images,reserve_price,zk_final_price,user_type,provcity,item_url,seller_id,volume,nick"
# req.q="女装"

# try:
# 	resp= req.getResponse()

# 	##返回json数据进行格式化后输出
# 	js = json.dumps(resp, sort_keys=True, indent=4, separators=(',', ':'))
# 	print(js)
# except Exception,e:
# 	print(e)


#好券清单API(工作不正常，待查)
req=top.api.TbkDgItemCouponGetRequest()
req.set_app_info(top.appinfo("25527845","a17bff452a120a8e4fd3ea8e4299fb14"))

req.platform = 2
req.adzone_id=20380356
# 商品的类目ID
# req.cat = "16,18"
# 每页返回的商品数量
req.page_size = 5

req.q = "python"
req.page_no = 1
# req.pid = mm_11592178_5816688_20380356

try:
	resp= req.getResponse()
	##返回json数据进行格式化后输出
	# js = json.dumps(resp, sort_keys=True, indent=4, separators=(',', ':'))
	# print(js)
	print resp
except Exception,e:
	print(e)