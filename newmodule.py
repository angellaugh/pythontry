# 用requests模块替换urllib的功能

import requests

url = 'http://www.cmall.com'
url_new = 'http://www.cmall.com/login.new.html'

# 获取网页，my company
r = requests.get(url)
ra = requests.get(url_new)
print(r.url)

# 获取网页编码，我司主页为：ISO-8859-1
print(r.encoding)

# 修改requests的编码形式
# r.encoding = 'utf-8'

# 查询网页状态码
print(r.status_code)
print(ra.status_code)

# 获取响应头内容
print(r.headers)
print(ra.headers)

# 获取请求头内容
print(r.request.headers)

# 自定义请求头
header1 = {'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}
rb = requests.get(url, headers=header1)
print('hello', rb.request.headers)

# 访问登录页面
data = {'loginAccount':'angel', 'password':'lantian', 'rememberMe':0}
rc = requests.get(url_new, params=data, headers=header1)
# rc = requests.post(url_new, data=data, headers=header1)
print(rc.url)
print(rc.text)

# 获取页面内容
r.text
r.content # 字节显示

# 一些用法
# r = requests.post("http://httpbin.org/post")
# r = requests.put("http://httpbin.org/put")
# r = requests.delete("http://httpbin.org/delete")
# r = requests.head("http://httpbin.org/get")
# r = requests.options("http://httpbin.org/get")


# rget = requests.get(ra,params=data)
# print(rget.url)


