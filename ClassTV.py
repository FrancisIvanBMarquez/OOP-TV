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
        
    # power