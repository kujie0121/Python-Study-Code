#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
服务器端，处理客户端请求并返回数据
'''

import socket
import threading, time

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口：
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 999...')

#服务器端处理信息
def udplink(data, addr):
	print('Received from %s:%s...' % addr)
	s.sendto(b'Hello, %s!' % data, addr)

while True:
	#接受一个新连接：
	data, addr = s.recvfrom(1024)
	#创建新县城来处理TCP连接：
	t = threading.Thread(target=udplink, args=(data, addr))
	t.start()