# pythontry
a little try

 "ctrl+shift+/"  大段注释！
 




<!-- splite -->
# 提交命令
1. git add file.py
2. git commit -m "I added a file"
3. git push -u aaa master
4. git stauts:当前关联的远程仓库名字


# 强制覆盖本地文件
git fetch --all  
git reset --hard origin/master 
git pull


# clone别人的仓库
git clone https://github.com/lilei/english


# python3 用 “w” is enough
file1 = open("LiveNews" + crFile + ".txt", 'w')
print(event.findNext('a').text, file = file1)
Don't forget, in python3 use w is enough, needn't wb or wt or others!

1.“写”模式会重写文件。传递mode='w'参数给open()函数。

2.“追加”模式会在文件末尾添加数据。传递mode='a'参数给open()函数。

