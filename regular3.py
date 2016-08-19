import re

#多行正则匹配
email = r'\w{3}@\w+(.com|\.cn)'  # 用|分组

p = re.match(email,'zzz@csvt.com')
print(p)

p1=re.findall(email,'zzz@csvt.com') # 只返回分组种的内容
print(p1)   



# 数据的规律
s = 'hhsdj dskj hello src=csvt yes jdakff src =123 yes sdfj src=234 yes askdf hello src=python yes ska'

r1 = r'hello src=(.+) yes'
p2 = re.finditer(r1,s)
print(p2)

