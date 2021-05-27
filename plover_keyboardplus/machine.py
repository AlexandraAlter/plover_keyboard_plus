from plover import _
from plover.machine.keyboard import Keyboard

from plover_keyboardplus.keyboardcontrol import KeyboardPlusCapture


# i18n: Machine name.
_._('Keyboard Plus')


class KeyboardPlus(Keyboard):
    KEYS_LAYOUT = KeyboardPlusCapture.SUPPORTED_KEYS_LAYOUT
    ACTIONS = ('arpeggiate',)
    
    def __init__(self, params):
        super().__init__(params)

    def start_capture(self):
        self._initializing()
        try:
            self._keyboard_capture = KeyboardPlusCapture()
            self._keyboard_capture.key_down = self._key_down
            self._keyboard_capture.key_up = self._key_up
            self._suppress()
            self._keyboard_capture.start()
        except:
            self._error()
            raise
        self._ready()
