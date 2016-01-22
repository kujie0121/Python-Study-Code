#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Metaclass(元类): 使用type和metaclass创建class.
'''

#最常见的方式来创建Class：
''''''''''''''''''''''''''''''''''''
class Hello(object):
    def hello(self, name = 'world'):
        print('Hello, %s' % name)

h = Hello()
print(h.hello())
''''''''''''''''''''''''''''''''''''

#使用type()函数动态创建Class：
''''''''''''''''''''''''''''''''''''
#定义一个函数：
def fn(self, name = 'world'):
    print('Hello2, %s' % name)

#使用type()函数动态创建Class：
#type(class的名称，集成度父类集合(tuple)，class的方法名称与函数绑定(dict))
Hello2 = type('Hello2', (object,), dict(hello = fn))
h2 = Hello2()
print(h2.hello())
''''''''''''''''''''''''''''''''''''

# 使用metaclass元类
''''''''''''''''''''''''''''''''''''
# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    #__new__(cls, *args, **kwargs) :创建对象时调用，返回当前对象的一个实例;注意：这里的第一个参数是cls即class本身.
    #__new__(当前准备创建的类的对象，类的名字，类继承的父类集合，类的方法集合):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return  type.__new__(cls, name, bases, attrs)

#当传入关键字参数metaclass时，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建；
# 在此，我们就可以修改类的定义了，如，加上新的方法，然后，返回修改后的定义。：
class MyList(list, metaclass=ListMetaclass):
    pass

L = MyList()
#普通的list没有add()方法的：
L.add(1)
L.add(2)
L.append(3)
print(L)
''''''''''''''''''''''''''''''''''''