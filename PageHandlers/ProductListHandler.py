
import tornado.web

from Controller.product_list import get_products_list


class ProductListHandler(tornado.web.RequestHandler):
    def get(self, category_name):
        if not category_name:
            data = get_products_list()
        else:
            data = get_products_list(category_name)
        self.set_header('content-type', 'application/json')
        self.write(data)
