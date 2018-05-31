import unittest
from fizz_numbers import *


class FizzNumbersTest(unittest.TestCase):
    def test_receive_value_1(self):
        self.assertEqual(fizz_numbers([1]), [1])

    def test_receive_list_two_values(self):
        list_two_values = [1, 2]
        self.assertEqual(fizz_numbers(list_two_values), [1, 2])

    def test_receive_first_number_tree(self):
        self.assertTrue('Three' in fizz_numbers(range(1,4)))
        self.assertEqual(fizz_numbers(range(1,4))[2], 'Three')

    def test_receive_first_number_five(self):
        self.assertTrue('Five' in fizz_numbers(range(1,6)))
        self.assertEqual(fizz_numbers(range(1,6))[4], 'Five')

    def test_reveive_first_number_treefive(self):
        self.assertTrue('ThreeFive' in fizz_numbers(range(1,16)))
        self.assertEqual(fizz_numbers(range(1,16))[14], 'ThreeFive')

    def test_get_last_number_tree(self):
        self.assertEqual(fizz_numbers(range(1,101))[-2], 'Three')

    def test_get_last_number_five(self):
        self.assertEqual(fizz_numbers(range(1,101))[-1], 'Five')

    def test_get_last_number_treefive(self):
        self.assertEqual(fizz_numbers(range(1,101))[-11], 'ThreeFive')


if __name__ == '__main__':
    unittest.main()
