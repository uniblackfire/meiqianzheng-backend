import unittest

from src.Controller.product_list import get_products_list, get_product_info_by_barcode, get_promotion_name_by_type


class product_list_test(unittest.TestCase):
    def setUp(self):
        # print('setUp...')
        pass

    def tearDown(self):
        # print('tearDown...')
        pass

    def test_get_products_list_output(self):
        self.assertIsNotNone(get_products_list())

    def test_get_product_info_by_barcode(self):
        item_dict = get_product_info_by_barcode('ITEM000005')
        self.assertEqual(item_dict['barcode'], 'ITEM000005')

    def test_get_promotion_name_by_type(self):
        result = get_promotion_name_by_type('BuyTwoGetOneFree')
        self.assertEqual(result, '买二赠一商品')
        result = get_promotion_name_by_type('ZHE_95')
        self.assertEqual(result, '95折')

if __name__ == '__main__':
    unittest.main()
