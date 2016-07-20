import json
import unittest

from Controller.order import get_items_dict, order_process


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

    def test_order_process(self):
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
        result = json.loads(order_process(input_data))
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    unittest.main()
