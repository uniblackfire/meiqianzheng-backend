import tornado.web


class OrderHandler(tornado.web.RequestHandler):
    def post(self):
        # 返回数据
        aaaa = self.get_argument('productsinfo')
        myjson = 'ok'
        self.write(myjson)
