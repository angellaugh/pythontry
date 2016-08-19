# -*- coding:gb2312 -*-
from html.parser import HTMLParser
from urllib.parse import urlparse

# from urllib.parse import urllib2



#import HTMLParser
#import urlparse
#import urllib2
#import cookielib

import urllib
import urllib.parse
import urllib.request
import urllib.response
import http.cookiejar
import string
import re

hosturl = 'http://www.cmall.com' # 登录的主页面
posturl ='http://www.cmall.com/login.new.html'# 从数据包中分析出处理post请求的url

# 设置一个cookie处理器，负责从服务器下载cookie到本地并在发送请求时带上本地cookie
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)


# 打开登录主页面，以下载cookie到本地，以后再送post时就可以用cookie了
h = urllib.request.urlopen(hosturl)

# 构造header,一般header要包含如下至少一项，从抓包工具中分析的
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'}

# 构造post数据，也是从抓包中分析出的
postData = {'loginAccount':'angel','password':'lantian','rememberMe':'1'}

# 需要给post数据编码
postData1 = urllib.parse.urlencode(postData).encode('utf-8')


# 通过urllib2提供的request方法来向指定url发送我们构造的数据，并完成登录
request1 = urllib.request.Request(url=posturl, data=postData1, headers=headers)
# print(request1)
response1 = urllib.request.urlopen(request1).read().decode('utf-8')
# text = response1.read().decode('UTF-8')
print(response1)

# save_path = 'D:\\aaa.txt'
# f_obj = open(save_path,'wb')
# f_obj.write(text)
# print('aaa successfully')


