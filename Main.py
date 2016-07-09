import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

import Constants
from PageHandlers.AdminHandlers.AdminHandler import AdminHandler
from PageHandlers.AdminHandlers.AdminSigninHandler import AdminSigninHandler
from PageHandlers.AdminHandlers.ColumnsHandler import ColumnsHandler
from PageHandlers.ArticleHandler import *
from PageHandlers.MainHandler import MainHandler, SectionModule

define("port", default=get_site_port(), help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        # important!!!!!
        handlers = [
            (r"/?", MainHandler),
            (r"/admin/?", AdminHandler),
            (r"/admin/columns", ColumnsHandler),
            (r"/admin/signin", AdminSigninHandler),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            ui_modules={
                'Section': SectionModule,
            },
            cookie_secret='ABCD0912bZJc2sWbQLKos4156GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=',
            xsrf_cookies=True,
            login_url='/admin/signin',
            debug=DEBUG_ENABLED,
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    Constants.init()
    # NOTE: start mongodb before run this web app
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
