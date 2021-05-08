from plover import _
from plover.machine.keyboard import Keyboard
from plover.oslayer.keyboardcontrol import KeyboardCapture


# i18n: Machine name.
_._('KeyboardPlus')

EXTRA_F_KEYS = 'F13 F14 F15 F16 F17 F18 F19 F20 F21 F22 F23 F23'


class KeyboardPlus(Keyboard):
    KEYS_LAYOUT = KeyboardCapture.SUPPORTED_KEYS_LAYOUT.replace('F12', 'F12 ' + EXTRA_F_KEYS)

