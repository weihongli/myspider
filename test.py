import tornado.options
import tornado.httpserver
import tornado.web
import tornado.ioloop
import os
from tornado.options import options, define

define("port", default=8082)


class pageHandler(tornado.web.RequestHandler):
	def get(self):
		self.render("form.html", Ans="")

	def post(self):
		num1 = int(self.get_argument("number1"))
		num2 = int(self.get_argument("number2"))
		op = self.get_argument("operator")
		try:
			if op == "+":
				ans = num1 + num2
			elif op == "-":
				ans = num1 - num2
			elif op == "*":
				ans = num1 * num2
			elif op == "/":
				ans = num1 / num2
			else:
				ans = "wrong"
		except Exception as m:
			ans = m
		finally:
			self.render("form.html", Ans=ans)


if __name__ == '__main__':
	tornado.options.parse_command_line()
	app = tornado.web.Application(
		handlers=[
			(r"/cal", pageHandler)
		],
		template_path=os.path.join(os.path.dirname(__file__), "pages")
	)
	http_server = tornado.httpserver.HTTPServer(app)
	http_server.listen(options.port)
	tornado.ioloop.IOLoop.instance().start()
