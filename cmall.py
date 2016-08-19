import urllib.request
import urllib
import urllib.parse
import http.cookiejar

ulr1='http://www.cmall.com/login.new.html'
# 获取cookie
cookie = http.cookiejar.CookieJar()
cookieProc = urllib.request.HTTPCookieProcessor(cookie)

# 更改网页打开的方式，用cookie
opener = urllib.request.build_opener(cookieProc)
urllib.request.install_opener(opener)



# 模拟浏览器登录
# 构造post数据，也是从抓包中分析出的
data = {'loginAccount':'angel', 'password':'lantian', 'rememberMe':0}
post_data = urllib.parse.urlencode(data).encode('utf-8')
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'}
request1 = urllib.request.Request(url=ulr1, data=post_data,headers=header)


res = urllib.request.urlopen(request1).read().decode('utf-8')



#如果上面代码没有install_opener()，则这里可用:opener.open(req).read()方法来获取内容。
print(res)