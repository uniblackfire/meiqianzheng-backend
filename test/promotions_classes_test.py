import unittest

from src.Controller.Promotion import Promotion


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

    def test_get_new_items_price_badminton_in_BuyTwoGetOneFree(self):
        badminton_promotion_instance = Promotion.get_promotion_class(
            'BuyTwoGetOneFree',
            '羽毛球',
            6.0,
            6,
            1.0,
            '个')
        self.assertEqual(badminton_promotion_instance.get_new_items_price(), 4.0)

    def test_get_new_items_price_badminton_in_ZHE95(self):
        banana_promotion_instance = Promotion.get_promotion_class(
            'Zhe95',
            '羽毛球',
            3.0,
            1,
            3.0,
            '斤')
        self.assertEqual(banana_promotion_instance.get_new_items_price(), 2.85)

    def test_get_promote_message(self):
        self.assertIsNotNone(self.promotion_instance.get_promote_message())

    def test_get_basic_info(self):
        self.assertIsNotNone(self.promotion_instance.get_basic_info())


if __name__ == '__main__':
    unittest.main()
