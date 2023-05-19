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
tv1.turn_on()


# call TV2 and print channel and volume
tv2 = TV(0, 0, True)

# set channel
tv2.set_channel(4)
# channel down
tv2.channel_down()
# set volume
tv2.set_volume(3)
# volume down
tv2.volume_down()
# turn off
tv2.turn_off()

# tv status
tv1.tv_status()
tv2.tv_status()

