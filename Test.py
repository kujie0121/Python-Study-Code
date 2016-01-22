#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python 的输入和输出
s = input('\\输入出生年份哦~ ：\n')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')	

#Python 的循环
#range()函数可生成一个整数序列，通过list()函数可以转换为list,如：list(range(5))
sum = 0
for x in range(1,100,2):
	sum = sum + x
print(sum)


#Python 函数定义及引用，调用
import math
def quadratic(a, b, c):
	d = math.sqrt(b**2 - 4*a*c)
	x1 = (-b + d) / (2*a)
	x2 = (-b - d) / (2*a)
	return x1, x2
# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0)

#定义函数默认参数
def enroll(name, gender, age=6, city='Beijing'):
	print('name:',name)
	print('gender:',gender)
	print('age:',age)
	print('city:',city)
#测试：
enroll('Sarah','F')
enroll('BOB','M',7)
enroll('Adam','M',city='Tianjin')

#函数判断str，None 不变对象
def add_end(L=None):
	if L is None:
		L = []
	L.append('END')
	return L
#测试
add_end([1,2])
add_end()

#定义可变参数
#在函数内部，参数numbers接收到的是一个tuple
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
#测试
calc([1,2])
calc((1,2,3))
calc(1,3,5,7)
#直接传递List或Tuple
nums = [1,2,3]
calc(nums[0], nums[1], nums[2])
calc(*nums)

#定义关键字参数
#关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict。
def person(name,age,**kw):
	print('name:', name, 'age:', age, 'other:', kw)
#测试
person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
#直接传递数据字典dict
extra = {'city':'Beijing', 'job':'Engineer'}
person('Jack', 24, **extra)

#命名关键字参数（带默认值）
#和关键字参数**kw不同，命名关键字参数需要特殊分隔符*，*后面的参数被视为命名关键字参数。
def person2(name, age, *, city='Beijing', job):
	print(name, age, city, job)
#测试
person2('Jack', 24, job='Engineer')

#参数可组合使用，但参数定义的顺序必须是：必选参数、默认参数、可变参数/命名关键字参数和关键字参数
def F1(a, b, c=0, *args, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def F2(a, b, c=0, *, d, **kw):
	print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)	
#测试
F1(1, 2)
F1(1, 2, c=3)
F1(1, 2, 3, 'a', 'b')
F1(1, 2, 3, 'a', 'b', x=99)
F2(1, 2, d=88, ext=None)
#直接传递Dict和Tuple
args = (1, 2, 3, 4)
args2 = (1, 2, 3)
kw = {'d':88, 'x':'#'}
F1(*args, **kw)
F2(*args2, **kw)

#递归函数
#解决递归调用栈溢出的方法是通过尾递归优化,尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。
def fact(n):
	return fact_iter(n, 1)
def fact_iter(num, product):
	if num == 1:
		return product
	return fact_iter(num-1, num * product)
#return fact_iter(num - 1, num * product)仅返回递归函数本身，num - 1和num * product在函数调用前就会被计算，不影响函数调用。
#测试
fact(5)




