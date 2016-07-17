import tornado.web

from Controller.order import order_process


class OrderHandler(tornado.web.RequestHandler):
    def post(self):
        # 返回数据
        order_info = self.get_argument('order')
        result = order_process(order_info)
        self.write(result)
