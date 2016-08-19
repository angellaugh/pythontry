# -*- coding=utf-8 -*-
import urllib
import urllib.request

# def getdata():
# 	url = 'http://www.baidu.com'
# 	data = urllib.request.urlopen(url).read()
# 	print(data)

# getdata()
# print urllib.request.urlopen('http://www.baidu.com').read()

params = urllib.urlencode({'loginAccount':'angel','password':'lantian','rememberMe':1})
f = urllib.urlopen('http://www.cmall.com/memberSite/sso/loginJson?%s'%params)
print(f.read())