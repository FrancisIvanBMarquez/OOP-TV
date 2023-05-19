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
        self.channel = self.channel + 1
    
    def channel_down(self):
        self.channel = self.channel - 1
    
    # volume
    def get_volume(self):
        print(self.volume_level)
    
    def set_volume(self, new_volume):
        self.volume_level = new_volume

    def volume_up(self):
        self.volume_level = self.volume_level + 1
    
    def volume_down(self):
        self.volume_level =  self.volume_level - 1
    
    # power
    def turn_on(self):
        self.power_on = True

    def turn_off(self):
        self.power_on = False

    # check tv status
    def tv_status(self):
        print("Channel: ", self.channel, "\nVolume: ", self.volume_level, "\nTurned on: ", self.power_on)



    