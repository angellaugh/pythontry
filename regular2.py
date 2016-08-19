import re
r0 = r'^\d{3,4}-?\d{8}$' #要有起始^和结尾$才可以
r01 = r'^\d{3,4}-?\d{8}'
st0='010-12345678'
st01='010-123456788888'
p0=re.findall(r0,st0)
p00=re.findall(r0,st01)
p01=re.findall(r01,st0)
p011=re.findall(r01,st01)
print('又匹配首都的座机：',p0,p00,p01,p011)

p_tel = re.compile(r0) # 编译让匹配更快
print('编译正则表达式r0：',p_tel.findall('010-112345678'))
print('编译正则表达式r0：',p_tel.findall('010-12345678'))


#在匹配中不区分大小写用：re.I
#csvt_re = re.compile(r'CcSsVvTt')
csvt_re = re.compile(r'csvt',re.I)
print(csvt_re.findall('csvt CSVT cSVt CCsvt'))


print(csvt_re.match('csvt hello')) # match查找开头
print(csvt_re.match('hello'))
print(csvt_re.match('hello csvt'))

print(csvt_re.search('hello csvt')) # search 查找整个句子


x = csvt_re.finditer('hello csvt hello csvt csvt')
print(x)
#print(x.next()) 


s1 = 'hello csvt'
s11=s1.replace('csvt','python')
print(s11)

rs = r'c..t'
s2 = re.sub(rs,'python','csvt caat cvvt cccc')
#subn 输出时会显示一共替换了多少次
s3 = re.subn(rs,'python','csvt caat cvvt cccc')
print(s2,s3)

#split 切割
ip = '1.2.3.4'
s4 = ip.split('.')
print(s4)
data = '123+45+-6-789*000'
# +-*都有意义，所以要转义
s5 = re.split(r'[\+\-\*]',data)
print(s5)

