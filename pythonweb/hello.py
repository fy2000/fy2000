# -*- coding: utf-8 -*-

def application(environ, start_response):
    start_response("200 OK", [('Content-Type', 'text/html')])
    body = '<hi>你好！世界</h1>'
    return [body.encode('utf-8')]
