# -*- coding:utf-8 -*-
'''
   实现了用requests模块，登录到网站（自定义headers，url用的是登录的接口）
   实现了改变网页的编码方式，使其可以正常输汉字
   实现了输出漂亮json格式
   实现了保持登录状态，并添加用户信息的功能
   实现了获取地址list并展现为json格式的功能（其中传递了time（时间戳为13位）参数）
   实现了删除adressId功能，只能单个删除
   实现了正则匹配addressId，取出id，但是带：，不能用
   实现了统计当前addressId个数
   实现了取出id，bbb = aaa['result']['pageItems']
   实现了循环遍历，当个数=10，则删除9个地址，保留一个
'''


import requests
import urllib




url = 'http://www.cmall.com'
url_new = 'http://www.cmall.com/login.new.html'

# 登录用如下这个接口
url_second = 'http://www.cmall.com/memberSite/sso/loginJson'


# 自定义请求头
header1 = {'X-Requested-With': 'XMLHttpRequest', 'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
header2 = {'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 'cookie' : "{'JSESSIONID':'F41BFDF4D5A0E1C732D5AB03ACC116E6', '__lfcc':1, 'enshrines_key':0, 'User_id':'323805', 'User_code':0, 'nickName':'angel', 'loginAccount':'angel', 'location':'', 'iconUrl':'/img_sys/icon_head/head.png','roleId':2, 'regional':'CN', 'toKen':'b5327d5560a1374073d2e524052', '_ga':'GA1.2.317077138.1462514096', '_gat':1, 'Hm_lvt_6b905f228492484ca5d757ea626ddfbd':'1462440082,1462440953,1462444420,1462512477', 'Hm_lpvt_6b905f228492484ca5d757ea626ddfbd':'1462514266'}"}
header3 = {'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36', 'User_id':'323805', 'User_code':0, 'nickName':'angel', 'loginAccount':'angel', 'location':'', 'iconUrl':'/img_sys/icon_head/head.png','roleId':2, 'regional':'CN', 'toKen':'b5327d5560a1374073d2e524052'}


# 访问登录页面
data = {'loginAccount':'angel', 'password':'lantian', 'rememberMe':1}


# rc = requests.get(url_new, params=data, headers=header1)
rc = requests.post(url_second, data=data, headers=header1)




print(rc.url)
# 文本形式输出
print(rc.text)
# json形式输出
print(rc.json())

''' 重点！：输出json格式的response，干得漂亮！'''
''' 当只输出response时，返回的是状态码：<Response [200]>'''
from pprint import pprint
pprint(rc)
pprint(rc.json())

adurl = 'http://www.cmall.com/memberSite/memberAddress/addOrUp'
addata = {'shipperName':'啊哈哈哈哈', 'address':'囖囖囖猪', 'mobile':'11111111111', 'zip':'', 'isDefault':0, 'countryCode':'CN'}
# cookie1 = {'JSESSIONID':'F41BFDF4D5A0E1C732D5AB03ACC116E6', '__lfcc':1, 'enshrines_key':0, 'User_id':'323805', 'User_code':0, 'nickName':'angel', 'loginAccount':'angel', 'location':'', 'iconUrl':'/img_sys/icon_head/head.png','roleId':2, 'regional':'CN', 'toKen':'b5327d5560a1374073d2e524052', '_ga':'GA1.2.317077138.1462514096', '_gat':1, 'Hm_lvt_6b905f228492484ca5d757ea626ddfbd':'1462440082,1462440953,1462444420,1462512477', 'Hm_lpvt_6b905f228492484ca5d757ea626ddfbd':'1462514266'}



import requests.cookies
import datetime
import time

'''在请求的参数中加上 登录请求(第一次请求) 时的cookie，就可以解决errologin的问题啦'''
'''试过session，试过自己制造cookie，都不行'''
aduu = requests.get(adurl, params=addata, headers=header3, cookies=rc.cookies)
# # aduu = requests.get(adurl, params=addata, headers=header3, cookies=cookie1)
#
print(aduu.url)
print(aduu.text)
pprint(aduu.json())


ticks = time.time()

''' 13位时间戳'''
ticks13 = int(ticks*1000)
print('当前时间戳:', ticks)
print('13位时间戳:', ticks13)

''' 将13位时间戳转换为当前时间'''
local_str_time1 = datetime.datetime.fromtimestamp(ticks13 / 1000.0)
print('local_str_tme1:', local_str_time1)

data_time = {'time':ticks13}

urladlist = 'http://www.cmall.com/memberSite/memberAddress/list'
gtadlist = requests.get(urladlist, headers=header3, cookies=rc.cookies, params=data_time)




# 检查获取网页的编码，发现是ISO-8859-1，然后重写为utf-8
print(gtadlist.encoding)
gtadlist.encoding = 'utf-8'
print(gtadlist.encoding)



print(gtadlist.url)
print(gtadlist.history)
print(gtadlist.text)
# print(gtadlist.json())


pprint(gtadlist.json())

import json

aaa = gtadlist.json()
bbb = aaa['result']['pageItems']
print('hello', bbb)
print('博客园小伙伴赞助pageItems包含的个数判定：', len(bbb))
x = len(bbb)
urldel = 'http://www.cmall.com/memberSite/memberAddress/del'


#  无限循环不跳出去了 囧
#  分别尝试了用x，用len(bbb)等做计数，都无效，最后使用y，y还不可以写在for循环内。
#  然后，for循环可以跳出了，发现while循环还在，最终算是解决了！！！
while x == 10:
    y = 0
    for item in bbb:
        print('by loveisbug@cnblogs赞助遍历', item['addressId'])
        delad = requests.get(urldel, headers=header3, cookies=rc.cookies, params={'addressId':item['addressId']})  # print(delad.url)
        print('try it !!!', delad.json())
        y = y +1
        print('计数器显示：', y)
        if y==9:
            break
    break








'''输出为： <map object at 0x00000281DCF47198>？？？'''
# print('北京annie赞助map方法：', map(bbb, item['addressId']))





'''http://www.cmall.com/memberSite/memberAddress/del?addressId=569'''
'''判断地址数量是否=10，如果是，则删除全部。'''


# 取出addressId并且计算个数
import re
radlist = r':\d{3}'
result = re.findall(radlist, gtadlist.text)
print('addressIds:', result)
# 计算地址个数
num = len(result)
print('现在的地址个数为:', num)
print('len(bbb):', len(bbb))

# if num == 10, x!=0:
# 	for x=10, y=0:
# 		delet num[y]
# 		x=x-1
# 		y=y+1
#
# else:








data_del = {'addressId':617}
# urldel = 'http://www.cmall.com/memberSite/memberAddress/del'
# delad = requests.get(urldel, headers=header3, cookies=rc.cookies, params=data_del)
# print(delad.url)
# print(delad.json())


# 把地址列表页的内容存储起来
savedata = gtadlist.text.encode('utf-8')
def saveFile(savedata):
	save_path= 'D:/temp.txt'
	f_obj = open(save_path, 'wb') # 打开文件的方式
	f_obj.write(savedata)
	f_obj.close()
saveFile(savedata)




'''
BeautifulSoup 大大方便了我们对抓取的 HTML 数据的解析,
可以用tag, class, id来定位我们想要的东西, 可以直接提取出正文信息,
可以全文搜索, 同样也支持正则表达式, 相当给力.

'''
# import requests
# from bs4 import BeautifulSoup
#
# response = requests.get('http://www.cmall.com')
# response.encoding = 'utf-8'
# soup = BeautifulSoup(response.text)
# soup1 = BeautifulSoup(gtadlist.text)
#
# print(soup.title.text)
# print(soup.body.text)
# print(soup.markup)
#
# # print(soup1.markup())
# # for x in soup1.findAll('addressId'):
# # 	print(x['addressID'])
#
#
#
