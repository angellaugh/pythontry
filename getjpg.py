import re #?正则表达式
import urllib # 获取源代码
import urllib.request

def getHtml(url):
    page=urllib.request.urlopen(url) #打开页面
    html=page.read() # 读取页面的数据
    return html
# print(getHtml('http://image.baidu.com/'))

def getImg(html):
	reg = r'src="(.*?\.jpg)"'
	imgre = re.compile(reg)
	imglist = re.findall(imgre,html)
	return imglist
	# for  imgurl  in imglist:
	# 	urllib.urlretrieve(imgurl,'1.jpg')
	x = 0
	for imgurl in imglist:
		urllib.urlretrieve(imgurl,'%s.jpg' % x)
        


html =  getHtml('http://image.baidu.com/')
getImg(html)
