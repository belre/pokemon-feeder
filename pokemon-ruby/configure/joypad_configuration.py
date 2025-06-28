import os, sys

sys.path.append("../")

from joykey import JoyKey
from joykey_feeder import VirtualJoyPad, VirtualFeeder
from wait_events import JoypadConfigureInitWaitEvent

import argparse
import time


"""
parser = argparse.ArgumentParser()
args = parser.add_argument('key')

args = parser.parse_args()

selected_key = JoyKey.find(args.key.upper())
if selected_key is None:
    print("Key name error")
    sys.exit(1)
"""

joypad = VirtualJoyPad(1)

JoypadConfigureInitWaitEvent().run()

feeder = VirtualFeeder(joypad)

keys = JoyKey.all_keys()
for key in keys:
    feeder.feed_button(key)




"""
# Pythonic API, item-at-a-time
j = vjoy.VJoyDevice(1)

# turn button number 15 on
j.set_button(15, 1)

# Notice the args are (buttonID,state) whereas vJoy's native API is the other way around.


# turn button 15 off again
j.set_button(15, 0)

# Set X axis to fully left
j.set_axis(vjoy.HID_USAGE.X, 0x1)

# Set X axis to fully right
j.set_axis(vjoy.HID_USAGE.X, 0x8000)




# Also implemented:

j.reset()
j.reset_buttons()
j.reset_povs()
"""

# The 'efficient' method as described in vJoy's docs - set multiple values at once

#print(j._data)
# >> > <pyvjoystick.vjoy._sdk._JOYSTICK_POSITION_V2 at 0x.... >


