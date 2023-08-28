from unittest import TestCase

from americana.bank import area


class Test(TestCase):

    def test_values(self):
        self.assertRaises(ValueError, area, -1)
        self.assertRaises(ValueError, area, -5)

    def test_radius_type(self):
        self.assertRaises(TypeError, area, True)
        self.assertRaises(TypeError, area, 2 + 5j)
