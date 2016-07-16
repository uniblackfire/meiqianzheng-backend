import tornado.web


class ProductInfoHandler(tornado.web.RequestHandler):
    def get(self, code):
        # 返回数据
        aaaa = code  # self.get_argument('code')

        self.write(aaaa)
