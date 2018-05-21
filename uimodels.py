#!/usr/bin/env python
#-*- coding:utf-8 -*-
__author__ = 'talus'

# import sys
#
# reload(sys)
# sys.setdefaultencoding('utf-8')

from tornado.web import UIModule


# class CustomModule(UIModule):
#     def calc(self):
#         return "calc"

class Advertisement(UIModule):
    def render(self, *args, **kwargs):
        return "1234"

    def css_files(self):
        return "/static/css/King_Chance_Layer7.css"

    def javascript_files(self):
        return [
            "/static/js/jquery_1_7.js",
            "/static/js/King_Chance_Layer.js",
            "/static/js/King_layer_test.js"
        ]