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
    def GetChannel(self):
        print(self.channel)
    # volume
    # power