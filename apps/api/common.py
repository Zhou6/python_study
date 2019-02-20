#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import ujson as json
except ImportError:
    import json

import tornado.web


class BareboneHandler(tornado.web.RequestHandler):
    """底层的handler 用以解决各个资源组件连接"""

    def __init__(self, application, request, **kwargs):
        # 处理
        super(BareboneHandler, self).__init__(application, request, **kwargs)
        if request.headers.get("cdn-src-ip", None):
            request.remote_ip = request.headers["cdn-src-ip"]
        elif request.headers.get("X-Forwarded-For", None):
            try:
                request.remote_ip = request.headers["X-Forwarded-For"].split(",")[0]
            except Exception as e:
                print e

    def write_error(self, status_code, **kwargs):
        super(BareboneHandler, self).write_error(status_code, **kwargs)

    @property
    def log(self):
        return self.application.log

    def write_json(self, obj):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(obj)


class BaseHandler(BareboneHandler):
    """基础handler 类"""
    pass