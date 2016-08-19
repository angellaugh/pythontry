
# -*- coding: utf-8 -*-
#coding:utf-8
'''
实现了通过app 获取网站首页内容；
实现了json打印出来结果，并decode了汉字显示
复习了pprint的漂亮json格式
实现了jdata筛选2层结果
实现了list中取出goodsName

'''

import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import requests
from pprint import pprint



# html = urlopen("http://www.cmall.com/page/CN/shop.html")
# print (html.read())
# bsobj = BeautifulSoup(html.read(), "html.parser")
# print (bsobj.title)
# print (bsobj.body)
# categorylist = bsobj.findAll("span", {"ng-bind":"interest.name", "class":"ng-binding"})
# print (categorylist)
# for categoryname in categorylist:
#     print (categoryname.get(text))



mhtml = urlopen("https://app.cmall.com/goodsSite/market/getAppMarketHome?abbr=CN&build=97&clientType=ios&clientVersion=1.4.4&customerId=88896133&dBrand=apple&dModel=iPhone%205&imagePHeight=568&imagePixels=640&oneCategoryCode=100&osVersion=iOS%209.3.2&pageNo=1&pageSize=30&recordsNumber=0&st=1471327694367&udid=18963fcf9c139612ddd716406ce58802c67f5f20")
mhtml1 = mhtml.read()
# print (mhtml.encoding)
# json.loads(request.b‌​ody.decode('utf-8'))
# data = urllib.parse.urlencode(msg)
# binary_data = data.encode('utf8')
# jdata['result']['pageItems']
# print (mhtml1)
# print (json.loads(mhtml1.decode()))
pprint(json.loads(mhtml1.decode()))
jdata = json.loads(mhtml1.decode())
aa = jdata['result']['pageItems']
for aaa in aa:
    print(aaa['goodsName'])
a = "你是对的"
print (a)
print("you are right|")

# cartpage =BeautifulSoup(mhtml1, "html.parser")
# cartlist = cartpage.findAll("goodsName")
# for goodsname1 in cartpage:
#     print (goodsname1.text())



# import lxml
# import requests     # 导入requests模块
# request_url = 'http://www.cmall.com/page/CN/shop.html'  # 请求的url是 上一章的url地址
# response = BeautifulSoup(requests.get(request_url).text , 'lxml')  # 请求并返回结果
# print(response.findAll)





# import requests
# from bs4 import BeautifulSoup
#
# html = requests.get("http://www.cmall.com/page/CN/shop.html")
# bsobj = BeautifulSoup(html, "html.parser")
# categorylist = bsobj.find("span", {"ng-bind":"category.name", "class":"ng-binding"})
# print (categorylist.text)
