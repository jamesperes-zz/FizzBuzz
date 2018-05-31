import unittest
from fizz_numbers import *


class FizzNumbersTest(unittest.TestCase):
    def test_receive_value_1(self):
        self.assertEqual(fizz_numbers([1]), [1])

    def test_receive_list_two_values(self):
        list_two_values = [1, 2]
        self.assertEqual(fizz_numbers(list_two_values), [1, 2])

    def test_receive_first_number_tree(self):
        list_values = range(1,4)
        self.assertEqual(fizz_numbers(list_values)[2], 'Three')





if __name__ == '__main__':
    unittest.main()
