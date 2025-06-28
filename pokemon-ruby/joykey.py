
from enum import IntEnum

class JoyKey(IntEnum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4
    BUTTON_A = 5
    BUTTON_B = 6
    BUTTON_L = 7
    BUTTON_R = 8
    SELECT = 9
    START = 10
    SPEED = 11
    CAPTURE = 12
    GS = 13

    @staticmethod
    def find(str: str):
        return JoyKey[str] if str in [joykey.name for joykey in JoyKey] else None

    @staticmethod
    def all_keys():
        return [ joykey for joykey in JoyKey]