import unittest
from unittest import mock

from Controller.database import read_products_list_file
from Controller.product_list import get_products_list


class product_list_test(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_get_products_list_output(self):
        self.assertIsNotNone(get_products_list())


if __name__ == '__main__':
    unittest.main()
