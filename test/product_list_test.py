import unittest
from unittest import mock

from Controller.database import read_products_list_file
from Controller.product_list import add_promotion_type_to_products_list


class product_list_test(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_products_list_should_have_promotion_type(self):
        pass
        # self.assertIsNotNone(obj['promotionType'])


if __name__ == '__main__':
    unittest.main()
