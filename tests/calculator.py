import unittest
from src import calculator
import pprint
from unittest import mock
from unittest.mock import patch, PropertyMock


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_load(self):
        self.calculator.load('../data/input1.json')
        self.assertEqual(6, len(self.calculator.get_data()))

    def test_process(self):
        self.calculator.load('../data/input1.json')
        self.calculator.process_data()
        self.assertEqual(6, len(self.calculator.get_res_json()))

    def test_res(self):
        self.calculator.load('../data/input1.json')
        self.calculator.process_data()
        self.assertEqual(1, self.calculator.get_count('Overweight'))
        self.assertEqual(2, self.calculator.get_count('Normal weight'))
        self.assertEqual(3, self.calculator.get_count('Moderately obese'))
        self.assertEqual(None, self.calculator.get_count('Severely obese'))
        self.assertEqual(None, self.calculator.get_count('Very severely obese'))

if __name__ == '__main__':
    unittest.main()
