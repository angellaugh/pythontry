# -*- coding:utf-8 -*-

#对内存的利用

a = [1,2,3,'a','b','c']

b = a #把a的值取出来赋给b

#值一样，内存空间也一样，a和b指向的地址空间一样
print(a,b)
print(id(a),id(b))


#改变a,改变b，两者都一起改变，因为地址空间一样
a.append('d')
print(a,b)
b.append('4')
print(a,b)

import copy # 让a和b地址空间变化，不再关联
c = [1,2,3,'a','b','c']
d = c
e = copy.copy(c)

print(c,d,e)
print(id(c),id(d),id(e))


#e不会改变
c.append('ff')
print(c,d,e)
#但是c的第一个元素地址，与e的第一个元素地址一样
print(id(c[0]),id(e[0]))

#如果要改变第一个元素的值，则e也跟着改变

#数字，字符串不可变类型，列表可变类型
#c的列表中增加元素，则e也跟着增加

#深copy，要copy所有的数据包括列表

a1 = [1,2,3,['a','b','c','d'],'d']
d1 = copy.deepcopy(a1)
print(id(a1),id(d1))  #地址不一样
print(id(a1[0]),id(d1[0]))  #不可变的数字、字符串，地址一样
print(id(a1[3]),id(d1[3]))  #可变的列表，地址不一样

#增加e，d1不受影响
a1.append('e')
print(a1,d1)

#增加列表中的x，d1不受影响
a1[3].append('x')
print(a1,d1)