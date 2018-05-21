#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'talus'

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')


import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

import uimethods as mt
import uimodels as md


settings = {
    'template_path': 'template',
    'static_path': 'static',
    'static_url_prefix': '/static/',
    'ui_methods': mt,
    'ui_modules': md,
}


class IndexHandler(tornado.web.RequestHandler):

    def func1(self):
        return "11111"

    def get(self, *args, **kwargs):
        #第一种方式
        self.render("index.html", func=self.func1)

app = tornado.web.Application(handlers=[
    (r"^/$",IndexHandler),
], **settings)

server = tornado.httpserver.HTTPServer(app)
server.listen(8082)

tornado.ioloop.IOLoop.instance().start()