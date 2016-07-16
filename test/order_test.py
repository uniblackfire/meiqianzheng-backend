import unittest
from unittest import mock

from Controller.database import read_products_list_file
from Controller.order import get_items_dict
from Controller.product_list import get_products_list


class order_test(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_get_items_dict(self):
        input_data = '''
        [

    'ITEM000001',

    'ITEM000001',

    'ITEM000001',

    'ITEM000001',

    'ITEM000001',

    'ITEM000003-2',

    'ITEM000005',

    'ITEM000005',

    'ITEM000005'

]



        '''
        result_dict = get_items_dict(input_data)
        self.assertIs(result_dict['ITEM000001'], 5)
        self.assertIs(result_dict['ITEM000003'], 2)
        self.assertIs(result_dict['ITEM000005'], 3)


if __name__ == '__main__':
    unittest.main()
