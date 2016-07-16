import tornado.web

from Controller.product_list import add_promotion_type_to_products_list


class ProductListHandler(tornado.web.RequestHandler):
    def get(self):
        # read in all products information
        # read_in_database()

        data = add_promotion_type_to_products_list()
        self.set_header('content-type', 'application/json')
        self.write(data)
