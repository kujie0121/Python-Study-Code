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

import asyncio

#@asyncio.coroutine
async def wget(host):
    print('wget %s...' % host)
    #asyncio.open_connection()返回一个(StreamReader, StreamWriter)实例对：
    connect = asyncio.open_connection(host, 80)
    #reader, writer = yield from connect
    reader, writer = await connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    #刷新底层的写缓冲区：
    #yield from writer.drain()
    await writer.drain()
    while True:
        #line = yield from reader.readline()
        line = await reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    #Ignore the body, close the socket
    writer.close()

# 获取EventLoop:
loop = asyncio.get_event_loop()
tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# 执行coroutine(协程)：
#asyncio.wait()，通过它可以获取一个协同程序的列表，同时返回一个将它们全包括在内的单独的协同程序:
loop.run_until_complete(asyncio.wait(tasks))
#关闭event loop：
loop.close()
