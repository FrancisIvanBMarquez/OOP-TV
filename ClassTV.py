# Marquez, Francis Ivan B.,_BSCpE 1-5

# class
class TV:
    # constructor
    def __init__(self, channel, volume_level, power_on):
        self.channel = channel
        self.volume_level = volume_level
        self.power_on = power_on
    # behaviors
    # channel
    def get_channel(self):
        print(self.channel)
    
    def set_channel(self, new_channel):
        self.channel = new_channel

    def channel_up(self):
        return self.channel + 1
    
    def channel_down(self):
        return self.channel - 1
    
    # volume
    def get_volume(self):
        print(self.volume_level)
    
    def set_volume(self, new_volume):
        self.volume_level = new_volume

    def volume_up(self):
        return self.volume_level + 1
    
    def volume_down(self):
        return self.volume_level - 1
    
    # power
    def turn_on(self):
        self.power_on = True

    def turn_off(self):
        self.power_on = False

    