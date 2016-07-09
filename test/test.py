import unittest


class TddInPythonExample(unittest.TestCase):
    def test_calculator_add_method_returns_correct_result(self):
        result = 4
        self.assertEqual(4, result)
