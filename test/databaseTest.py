import unittest
from unittest import mock

from Controller import database


class databaseTest(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_database_read_products_list(self):
        self.assertIsNotNone(database.read_products_list_file())


if __name__ == '__main__':
    unittest.main()
