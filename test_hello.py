import unittest
from hello import sum_of_two_numbers
class TestSumOfTwoNumbers(unittest.TestCase):
    def test_sum_positive_numbers(self):
        self.assertEqual(sum_of_two_numbers(5, 7), 12)
    def test_sum_negative_numbers(self):
        self.assertEqual(sum_of_two_numbers(-3, -7), -10)
    def test_sum_positive_and_negative_numbers(self):
        self.assertEqual(sum_of_two_numbers(5, -3), 2)
    def test_sum_with_zero(self):
        self.assertEqual(sum_of_two_numbers(0, 10), 10)
        self.assertEqual(sum_of_two_numbers(6, 0), 6)
    def test_sum_two_zeros(self):
        self.assertEqual(sum_of_two_numbers(0, 0), 0)
if __name__ == '__main__':
    unittest.main()