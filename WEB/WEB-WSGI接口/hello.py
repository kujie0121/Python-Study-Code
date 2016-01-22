#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def application(environ, start_response):
      start_response('200 OK', [('Content-Type', 'text/html')])
      #直接返回URL的“http://localhost:8000/”后半部分
      body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
      return  [body.encode('utf-8')]

