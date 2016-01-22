#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
服务器端，处理客户端请求并返回数据
'''

import socket
import threading, time

#创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#绑定端口：
s.bind(('127.0.0.1', 9999))
#监听端口，指定等待连接的最大数量：
s.listen(5)
print('Waiting for connection...')

#服务器端处理信息
def tcplink(sock, addr):
	print('Accept new connection from %s:%s...' % addr)
	sock.send(b'Welcome!')
	while True:
		data = sock.recv(1024)
		time.sleep(1)
		if not data or data.decode('utf-8') == 'exit':
			break
		sock.send(('Hello, %s!' % data).encode('utf-8'))
	sock.close()
	print('Connection from %s:%s closed.' % addr)


while True:
	#接受一个新连接：
	sock, addr = s.accept()
	#创建新县城来处理TCP连接：
	t = threading.Thread(target=tcplink, args=(sock, addr))
	t.start()