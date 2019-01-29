import tornado.options
import tornado.httpserver
import tornado.web
import tornado.ioloop
import os
from tornado.options import options, define
from Settings.WebSetting import configuration


define("port", default=configuration["port"])


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
