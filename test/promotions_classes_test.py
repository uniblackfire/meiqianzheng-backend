import unittest
from unittest import mock

from Controller.Promotion import Promotion
from Controller.database import read_products_list_file
from Controller.order import get_items_dict, order_process
from Controller.product_list import get_products_list


class order_test(unittest.TestCase):
    def setUp(self):
        self.promotion_instance = Promotion.get_promotion_class(
            'BuyTwoGetOneFree',
            '可口可乐',
            9.0,
            3,
            3.0,
            '瓶')

    def tearDown(self):
        # print('tearDown...')
        pass

    def test_get_new_items_price_coke(self):
        self.assertEqual(self.promotion_instance.get_new_items_price(), 6.0)

    def test_get_new_items_price_badminton(self):
        badminton_promotion_instance = Promotion.get_promotion_class(
            'BuyTwoGetOneFree',
            '羽毛球',
            6.0,
            6,
            1.0,
            '个')
        self.assertEqual(badminton_promotion_instance.get_new_items_price(), 4.0)

    def test_get_promote_message(self):
        self.assertIsNotNone(self.promotion_instance.get_promote_message())

    def test_get_basic_info(self):
        self.assertIsNotNone(self.promotion_instance.get_basic_info())


if __name__ == '__main__':
    unittest.main()
