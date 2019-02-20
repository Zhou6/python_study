#!/usr/bin/python
# -*- coding: utf-8 -*-

# pre path
import os

import settings

os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = "cpp"
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION_VERSION'] = "2"

import logging
import site  # 加载三方资源库，python1.5a3以上版本不需要写这一行，会自动加载
import os.path
import sys
from tornado.options import parse_command_line

ROOT = os.path.abspath(os.path.dirname(__file__))
# path = lambda *a: os.path.join(ROOT, *a)
# site.addsitedir(path('vendor'))

import tornado.httpserver
import tornado.ioloop
import tornado.web
from lib.routes import route


class Application(tornado.web.Application):
    def __init__(self):
        # 初始化路由
        handlers = route.get_routes()

        # 应用程序设置
        app_settings = dict(
            debug=True,
            autoescape=None,
            cookie_secret="WERSDFASDFSF233423423#@$@#$@#$@#$#@$#@dsfsafd",
            gzip=True,
            template_path=os.path.join(ROOT, "template")
        )

        tornado.web.Application.__init__(self, handlers, **app_settings)


# 导入所有的handler
for app_name in settings.APPS:
    # 加载 init_handlers.py
    __import__('apps.%s' % app_name, globals(), locals(), ['init_handlers'], -1)


def main():
    parse_command_line()
    _port = settings.API_PORT if len(sys.argv) == 1 else int(sys.argv[1])

    application = Application()
    http_server = tornado.httpserver.HTTPServer(application, xheaders=True)
    logging.info("API server Starting on port %d" % _port)
    # application.listen(10080)
    try:
        http_server.bind(_port)
        http_server.start()
    except Exception as e:
        print "message :%s  port:%s" % (e, _port)

    try:
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        logging.info("exiting...")
        sys.exit(0)


if __name__ == "__main__":
    main()