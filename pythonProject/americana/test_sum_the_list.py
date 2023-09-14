from unittest import TestCase

from americana.sum_the_list import sum_list


class Test(TestCase):
    def test_sum_list(self):
        numbers = [5, 4, 9, 7, 2, 0]
        value = 12
        result = sum_list(numbers, value)
        self.assertEqual(result, [0, 3])
