#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
aiohttp则是基于asyncio实现的HTTP框架。

案例为一个HTTP服务器，分别处理以下URL：
1. / - 首页返回b'<h1>Index</h1>'；
2. /hello/{name} - 根据URL参数返回文本 hello, %s!。
'''

import asyncio
from aiohttp import web

async def index(request):
      #相当于模拟耗时操作：
      await asyncio.sleep(0.5)
      #aiohttp.web.Response()：从StreamResponse继承，接收参数来设置HTTP响应内容并返回响应：
      return web.Response(body=b'<h1>Index</h1>')

async def hello(request):
      await asyncio.sleep(0.5)
      text = '<h1>hello, %s!</h1>' % request.match_info['name']
      return web.Response(body=text.encode('utf-8'))

async def init(loop):
      #aiohttp.web.Application()是一个字典类型的对象，可以通过‘请求处理程序’返回对应数据：
      app = web.Application(loop=loop)
      #router.add_route()增加响应规则；即设置请求条件(请求方式，路径等...)和对应的处理程序：
      app.router.add_route('GET', '/', index)
      app.router.add_route('GET', '/hello/{name}', hello)
      #loop.create_server()利用asyncio创建TCP服务：
      #make_handler()创建HTTP协议处理器来处理请求：
      srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
      print('Server started at http://127.0.0.1:8000...')
      return srv

# 获取EventLoop:
loop = asyncio.get_event_loop()
# 执行coroutine(协程)：
loop.run_until_complete(init(loop))
#持续运行直到调用停止命令：
loop.run_forever()
