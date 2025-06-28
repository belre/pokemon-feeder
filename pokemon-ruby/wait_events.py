import time
from joykey import JoyKey

class JoypadConfigureInitWaitEvent:
    def run(self):
        print("Launch Configuration; after 5s, start auto-configuration")
        time.sleep(5)

class JoypadConfigureIntervalWaitEvent:
    _key: JoyKey
    def __init__(self, key: JoyKey):
        self._key = key    
    
    def run(self):
        print(f"reduce key event: {self._key.name}")
        time.sleep(0.5)



