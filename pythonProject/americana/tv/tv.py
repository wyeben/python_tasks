class TV:
    def __init__(self):
        self.channel = 0
        self.volume_level = 0
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def set_channel(self, channel):
        if self.is_on:
            self.channel = channel

    def get_channel(self):
        if self.is_on:
            return self.channel
        return None

    def channel_up(self):
        if self.is_on:
            self.channel += 1

    def channel_down(self):
        if self.is_on and self.channel > 0:
            self.channel -= 1

    def set_volume(self, volume_level):
        if self.is_on:
            self.volume_level = volume_level

    def get_volume(self):
        if self.is_on:
            return self.volume_level
        return None

    def volume_up(self):
        if self.is_on and self.volume_level < 100:
            self.volume_level += 1

    def volume_down(self):
        if self.is_on and self.volume_level > 0:
            self.volume_level -= 1
