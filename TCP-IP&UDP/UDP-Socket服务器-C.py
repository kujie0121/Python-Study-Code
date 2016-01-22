#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
客户端，发起请求并接收数据
'''

#导入socket库：
import socket
#创建一个socket：
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for data in [b'Michael', b'Tracy', b'Sarah']:
    #发送数据：
    s.sendto(data, ('127.0.0.1', 9999))
    #接收返回数据：
    print('接收数据： ', s.recv(1024).decode('utf-8'))

#关闭连接：
s.close()
