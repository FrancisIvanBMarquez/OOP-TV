# Marquez, Francis Ivan B.,_BSCpE 1-5

# import ClassTV
from ClassTV import TV

# call TV1 and print channel and volume
tv1 = TV(0, 0, False)

# set channel
tv1.set_channel(29)
# channel up
tv1.channel_up()
# set volume
tv1.set_volume(2)
# volume up
tv1.volume_up()
# turn on


# call TV2 and print channel and volume
tv2 = TV(0, 0, False)

# set channel
# channel down
# set volume
# volume down
# turn on

# testing grounds
print("channel: ", tv1.channel)
print("volume: ", tv1.volume_level)

