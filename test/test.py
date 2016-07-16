import unittest
from unittest import mock


class TddInPythonExample(unittest.TestCase):
    def setUp(self):
        print('setUp...')

    def tearDown(self):
        print('tearDown...')

    def test_calculator_add_method_returns_correct_result(self):
        result = 4
        self.assertEqual(4, result)


if __name__ == '__main__':
    unittest.main()
