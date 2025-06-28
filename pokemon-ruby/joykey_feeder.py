from pyvjoystick import vjoy
from joykey import JoyKey
from wait_events import JoypadConfigureIntervalWaitEvent
import time


class VirtualJoyPad:
    _rId : int
    def __init__(self, rId: int):
        self._rId = 1    

    @property
    def instance(self):
        return vjoy.VJoyDevice(1)

class VirtualFeeder:
    _joypad: VirtualJoyPad
    _key: JoyKey
    def __init__(self, joypad: VirtualJoyPad):
        self._joypad = joypad

    def feed_button(self, key: JoyKey):
        j = self._joypad.instance
        j.set_button(key.value, 1)
        JoypadConfigureIntervalWaitEvent(key).run()
        j.set_button(key.value, 0)


if __name__ == '__main__':
    key_condition = 'DOWN2'
    print(JoyKey.find(key_condition))
    print(JoyKey.all_keys())


