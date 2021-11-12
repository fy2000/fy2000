# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server
from hello import application

httpd = make_server('', 8081, application)
print('Servering http on 8081...')

httpd.serve_forever()
