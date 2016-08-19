import urllib.request
import urllib
import urllib.parse
import http.cookiejar

# # 用urlopen打开百度首页，读取内容（二进制的）
# html = urllib.request.urlopen('http://www.baidu.com')
#
# # 转换成utf-8 格式，并打印出来
# html1 = html.read().decode('utf-8')
# print(html1)
ulr1='http://reg.163.com/logins.jsp'
# 获取cookie
cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)

# 更改网页打开的方式，用cookie
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)



# 模拟浏览器登录
data = {'username':'asuna12@163.com','password':'lantian1218','type':1}
post_data = urllib.parse.urlencode(data).encode('utf-8')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'}
request1 = urllib.request.Request(url=ulr1, data=post_data,headers=header)


res = urllib.request.urlopen(request1).read().decode('UTF-8')



#如果上面代码没有install_opener()，则这里可用:opener.open(req).read()方法来获取内容。
print(res)