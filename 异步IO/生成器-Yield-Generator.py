#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
某个函数包含了yield，这意味着这个函数已经是一个Generator,yield是一个表达式(Expression)，通过send(msg)语句让它执行，
并直到下一个yield表达式处，再次调用会接着上次的位置继续执行;
send(msg)传递值msg给yield表达式并返回下一个yield表达式的参数,当第一次使用send(None)调用时，yield不执行，此时直接返回等待下一次send()调用；
注意：第一次调用时，需使用send(None)语句，不能使用send发送一个非None的值，否则会出错的，因为没有yield语句来接收这个值。
如：
------------------------------
def h():
    x = 'x'
    y = 'y'
    print('第一次输出！')
    #这里的(yield x)是一个表达式，它的值等于c.send(msg)传递过来的msg，所以m的值为'Fighting!!!'，返回值为’x‘：
    m = yield x   # m = 'Fighting!!!'
    pirnt(m)
    yield y

c = h()
m1 = c.send(None)   # m1 = ’x‘
d1 = c.send('Fighting!!!')  # m1 = ’y‘
print('We will never forget the date', m1, '.', d1)
--------
输出结果：
>>> 第一次输出！
>>> Fighting!!!
>>> We will never forget the date x . y
------------------------------
'''



def consumer():
    r = ''
    while True:
        #因为此处为无限循环，所以从send(None)开始，每次yield返回值后都会停留在此。
        #这里的(yield r)为一个表达式，值为send(msg)传递的msg，返回的为r的值，第一次send(None)时，yield直接返回r值后，便停止在这里：
        n1 = yield r

        #此处的判断条件其实一次都没有True过，也就是里面的代码没有被执行过：
        # 因为第一次调用send(None)时，在yield处直接返回等待下一次的send()调用了，返回的值为r=''，其后n1的值分别为1~5：
        if not n1:
            print('被执行过！')
            return

        print('[CONSUMER] Consuming %s...' % n1)
        #此处为了便于分析yield每次的返回值，让r的值每次都不同
        r = ' 200 OK ' + r

def produce(c):
    #c.send(None)启动生成器
    bb = c.send(None)   # bb = ''
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s' % n)
        #此处c.send(n)在传递完n的值后，每次都返回(yield r)的值，也就是r的值
        r1 = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r1)
    #关闭consumer
    c.close()

c = consumer()
produce(c)


