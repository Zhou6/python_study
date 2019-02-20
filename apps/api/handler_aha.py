# -*- coding: utf-8 -*-

from apps.api.common import BareboneHandler
from lib.routes import route


@route("/a")
class AhaHandler(BareboneHandler):
    def post(self, *args, **kwargs):
        return self.write_json({"error": 0,
                                "msg": "ok",
                                "data": 'aha'})

    def get(self, *args, **kwargs):
        return self.write_json({"error": 0,
                                "msg": "ok",
                                "data": 'aha'})