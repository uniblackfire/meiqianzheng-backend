import tornado.web


class ProductListHandler(tornado.web.RequestHandler):
    def get(self):
        # read in all products information
        data = 'datahere'
        # self.set_status(200)
        self.write(data)
