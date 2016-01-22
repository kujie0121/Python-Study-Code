#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
异步IO:
用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型，
然后在coroutine内部用yield from调用另一个coroutine实现异步操作。

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。
请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
1. 把@asyncio.coroutine替换为async；
2. 把yield from替换为await。
'''

import threading
import asyncio

#@asyncio.coroutine
async def hello():
      print('Hello world! (%s)' % threading.currentThread())
      #异步调用asyncio.sleep(1):
      #r = yield from asyncio.sleep(1)
      r = await asyncio.sleep(1)
      print('Hello again! (%s)' % threading.currentThread())

#获取Eventloop：
loop = asyncio.get_event_loop()
#封装两个coroutine为Task
tasks = [hello(), hello()]
#执行coroutine：
#asyncio.wait()，通过它可以获取一个协同程序的列表，同时返回一个将它们全包括在内的单独的协同程序:
loop.run_until_complete(asyncio.wait(tasks))
loop.close()