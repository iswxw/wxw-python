#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/5/19 13:34
# @Author  : wxw
# @Site    : https://www.liaoxuefeng.com/wiki/1016959663602400/1017805733037760
# @File    : wsgi_web_interface.py

# 从wsgiref模块导入:
from wsgiref.simple_server import make_server


# 直接输出 hello world
# http://localhost:8000/
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, web!</h1>']


# http://localhost:8000/path
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()
