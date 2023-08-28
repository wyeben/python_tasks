
import unittest

from americana.tv.tv import TV


class TestTV(unittest.TestCase):
    def setUp(self):
        self.tv = TV()

    def test_turn_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.is_on)

    def test_turn_off(self):
        self.tv.turn_on()
        self.tv.turn_off()
        self.assertFalse(self.tv.is_on)

    def test_set_get_channel(self):
        self.tv.turn_on()
        self.tv.set_channel(5)
        self.assertEqual(self.tv.get_channel(), 5)

    def test_channel_up(self):
        self.tv.turn_on()
        self.tv.set_channel(10)
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 11)

    def test_channel_down(self):
        self.tv.turn_on()
        self.tv.set_channel(8)
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel(), 7)

    def test_set_get_volume(self):
        self.tv.turn_on()
        self.tv.set_volume(50)
        self.assertEqual(self.tv.get_volume(), 50)

    def test_volume_up(self):
        self.tv.turn_on()
        self.tv.set_volume(80)
        self.tv.volume_up()
        self.assertEqual(self.tv.get_volume(), 81)

    def test_volume_down(self):
        self.tv.turn_on()
        self.tv.set_volume(30)
        self.tv.volume_down()
        self.assertEqual(self.tv.get_volume(), 29)