import requests

url = 'http://www.cmall.com'
url_new = 'http://www.cmall.com/login.new.html'

# 自定义请求头
header1 = {'Accept-Encoding': 'gzip, deflate, sdch', 'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4', 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'}


# 访问登录页面
data = {'loginAccount':'angel', 'password':'lantian', 'rememberMe':0}
rc = requests.get(url_new, params=data, headers=header1)
# rc = requests.post(url_second, data=data, headers=header1)
print(rc.url)
# 文本形式输出
print(rc.text)
# json形式输出
print(rc.json())
