from unittest import TestCase

from americana.create_tuple import create_tuple


class Test(TestCase):
    def test_create_tuple(self):
        list1 = [1, 2, 3, 4, 5]
        list2 = [6, 7, 8, 9, 10]
        result = [(1, 6), (2, 7), (3, 8), (4, 9), (5, 10)]
        check = create_tuple(list1,list2)
        self.assertEqual(check,result)
