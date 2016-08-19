import re # 正则表达式模块
#s = 'abc'  #定义一个字符串

s = r'abc' #定义正则条件

st = 'top  tip tqp twp tep'

w = r't[io]p'   # []中只要满足任何一个字母都可以匹配
y = re.findall(w,st)
p = re.findall(s,'aaaaaaaaa') #拿字符串与正则条件匹配
q = re.findall(s,'abcadfafdafabcdddd')

print(p,q,y) #打印出匹配成功的字符串,有p和q两个数组



xiangfan = r't[^io]p' #取[]中除了i和o的其他,如果^写在[]里的后面，则当成普通的符号处理
ss = re.findall(xiangfan,st) #拿字符串与正则条件相匹配
print('取除了top和tip之外的字符串：',ss)

s1='hello world ,hello boy'
r1 = r'^hello' #^匹配行首是hello的语句,虽然字符串中有两个hello，但是最终匹配成功并输出的只有行首的那个hello
p1 = re.findall(r1,s1)
print('匹配行首是hello的：',p1)

r2 = r'boy$' #$匹配行尾是boy的那个词提取出来
p2 = re.findall(r2,s1)
print('匹配行尾是boy的：',p2)


r3 = 't[abc$]'
st1= 'taae tbdd tc tax t'
p3 = re.findall(r3,st1)
print('[]中有$时并不起作用:',p3)


r4 = r'x[0-9A-Za-z]x'#匹配数字0到9字母大小写的a到z

st2='x1x,x2x,x3x,x9x,x1x,x2222x' #是单个字母的匹配，所以最后个字符串x2222x不被匹配

p4 = re.findall(r4,st2)
print('匹配一个范围:',p4)


r5 = r'^abc' #匹配行首是abc的那个词
st51='abc aa abc ^abc ^abc ^abc'
st52='aa abc'
st53='^abc'
p51 = re.findall(r5,st51)
p52 = re.findall(r5,st52)
p53 = re.findall(r5,st53)
print('处理^：',p51,p52,p53)

r6 = r'\^abc' #转义字符\把行首的^转义成普通符号
p61 = re.findall(r6,st51)
p62 = re.findall(r6,st52)
p63 = re.findall(r6,st53)
print('处理^:',p61,p62,p63)


r7 = r'\d'  #效果等于r'[0-9]'
r8 = r'\D'  #效果等于任何非数字字符：[^0-9]
r9 = r'\s'  #任何空白字符：[\t\n\r\f\v]
r10= r'\S'  #任何非空白字符：[^\t\n\r\f\v]
r11= r'\w'  #任何字母数字：[a-zA-Z0-9]  好强大
r12= r'\W'  #任何非字母数字字符：[^a-zA-Z0-9] 好强大，所有符号吧
st7 = '21345678979409897'
p7 = re.findall(r7,st7)
print('\d代表数字：',p7)


r13 = r'^010-\d\d\d\d\d\d\d\d' #\d表示数字，需要8个数字
r14 = r'^010-\d{8}' #\d表示数字，{8}表示重复8次
r14 = r'^010-\d{8}$' # 严格上说还要加上代表结尾的$符号
st13 = '010-54684545'

p13 = re.findall(r13,st13)
p14 = re.findall(r14,st13)
print('匹配北京的电话号码：',p13,p14)

r15 = r'ab*'    # * 将前面的字符重复0次到多次
p15 = re.findall(r15,'a')
p16 = re.findall(r15,'abbb')
print('*是将前面的字符重复0次到多次：',p15,p16)

r17 = r'ab+'  # +将前面的字符重复1次到多次
p17 = re.findall(r17,'a')
p18 = re.findall(r17,'abbb')
print('+是将前面的字符重复1次到多次：',p17,p18)


r19 = r'^010-\d{8}$'
r20 = r'^010-*\d{8}$'# -可有可无的话怎么处理
st19 = '010-12345678'
st20 = '01012345698'
st21 = '010----12345698' #这样的话，多个---也可以被打印出来，不完美
p19 = re.findall(r20,st19)
p20 = re.findall(r20,st20)
p21 = re.findall(r20,st21)
print('区号后的-可有可无如何实现：',p19,p20,p21)
r30 = r'^010-?\d{8}$'   # ?代表可有可无，0个或者1个都行
p30= re.findall(r30,st19)
p31= re.findall(r30,st20)
p32= re.findall(r30,st21)
print('区号后的-可有可无如何实现：',p30,p31,p32)


#贪婪模式，非贪婪模式
r0 = r'ab+'
p0 = re.findall(r0,'abbbbbbbbbbbbbb') #取最大匹配，是贪婪匹配
print('贪婪模式取最大匹配：',p0)
r01 = r'ab+?'
p01 = re.findall(r01,'abbbbbbbbbbbb') #取最小匹配，把问号放在重复后面
print('非贪婪模式取最小匹配：',p01)

#{m,n} 至少重复m次，至多重复n次
r02 = r'a{3,5}'
p02 = re.findall(r02,'aa') 
p021 = re.findall(r02,'aaaaaaa') 
p022 = re.findall(r02,'aaa') 
p023 = re.findall(r02,'aaaaaaaaa')  # 可以被分成1个5，1个4
print('至少重复至多重复：',p02,p021,p022,p023)