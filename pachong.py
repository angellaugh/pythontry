import urllib.request
import urllib

# url = 'http://douban.com'
# webPage = urllib.request.urlopen(url)
# data = webPage.read()
# # data = data.decode('UTF-8')
# print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())


# weburl = 'http://www.cmall.com'
# webheader = {'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586'}
# req1 = urllib.request.Request(url=weburl, data=None, headers={webheader})
# # req = urllib.request.Request(url=weburl,headers=webheader)
# webPage = urllib.request.urlopen(req1)
# data = webPage.read()
# data = data.decode('UTF-8')
# print(data)
# print(type(webPage))
# print(webPage.geturl())
# print(webPage.info())
# print(webPage.getcode())

# 这个居然OK的
import urllib.request
source_stram = urllib.request.urlopen("http://www.12306.cn/mormhweb/kyfw/")
#save_path="D:\\baiDuYun\\百度云\\Code\\DotNet\\Download\\Python\\testPythonFiles\\instance_snatch_web\\snatch2.txt"
save_path="D:\\snatch2.txt"
# save_path 's file unnecessary to be exist
f_obj = open(save_path,'wb')
f_obj.write(source_stram.read())
print("snatch successfully.")
