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

hosturl = 'http://www.cmall.com' # ��¼����ҳ��
posturl ='http://www.cmall.com/login.new.html'# �����ݰ��з���������post�����url

# ����һ��cookie������������ӷ���������cookie�����ز��ڷ�������ʱ���ϱ���cookie
cj = http.cookiejar.LWPCookieJar()
cookie_support = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(cookie_support,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)


# �򿪵�¼��ҳ�棬������cookie�����أ��Ժ�����postʱ�Ϳ�����cookie��
h = urllib.request.urlopen(hosturl)

# ����header,һ��headerҪ������������һ���ץ�������з�����
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'}

# ����post���ݣ�Ҳ�Ǵ�ץ���з�������
postData = {'loginAccount':'angel','password':'lantian','rememberMe':'1'}

# ��Ҫ��post���ݱ���
postData1 = urllib.parse.urlencode(postData).encode('utf-8')


# ͨ��urllib2�ṩ��request��������ָ��url�������ǹ�������ݣ�����ɵ�¼
request1 = urllib.request.Request(url=posturl, data=postData1, headers=headers)
# print(request1)
response1 = urllib.request.urlopen(request1).read().decode('utf-8')
# text = response1.read().decode('UTF-8')
print(response1)

# save_path = 'D:\\aaa.txt'
# f_obj = open(save_path,'wb')
# f_obj.write(text)
# print('aaa successfully')


