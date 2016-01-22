#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Python内置了一个WSGI服务器，这个模块叫wsgiref，运行效率一般，仅供开发和测试使用。
#从wsgiref模块导入：
from wsgiref.simple_server import make_server
#导入我们自己编写在hello.py的application函数：
from hello import application

#创建一个服务器，IP地址为空，端口8000，处理函数是application：
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
#开始监听HTTP请求：
httpd.serve_forever()


