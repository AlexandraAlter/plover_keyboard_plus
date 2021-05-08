from Xlib.ext import xinput
from Xlib.ext.ge import GenericEventCode

from plover.oslayer import xkeyboardcontrol as base
from plover.oslayer.xkeyboardcontrol import with_display_lock

KEYCODE_TO_KEY = {
        191: "F13",
        192: "F14",
        193: "F15",
        194: "F16",
        195: "F17",
        196: "F18",
        197: "F19",
        198: "F20",
        199: "F21",
        200: "F22",
        201: "F23",
        202: "F24",
}

KEYCODE_TO_KEY.update(base.KEYCODE_TO_KEY)

KEY_TO_KEYCODE = dict(zip(KEYCODE_TO_KEY.values(), KEYCODE_TO_KEY.keys()))

class KeyboardPlusCapture(base.KeyboardCapture):
    def _on_event(self, event):
        if event.type != GenericEventCode:
            return
        if event.evtype not in (xinput.KeyPress, xinput.KeyRelease):
            return
        assert event.data.sourceid in self._devices
        keycode = event.data.detail
        modifiers = event.data.mods.effective_mods & ~0b10000 & 0xFF
        key = KEYCODE_TO_KEY.get(keycode)
        if key is None:
            # Not a supported key, ignore...
            return
        # ...or pass it on to a callback method.
        if event.evtype == xinput.KeyPress:
            # Ignore event if a modifier is set.
            if modifiers == 0:
                self.key_down(key)
        elif event.evtype == xinput.KeyRelease:
            self.key_up(key)

    @with_display_lock
    def suppress_keyboard(self, suppressed_keys=()):
        suppressed_keys = set(suppressed_keys)
        if self._suppressed_keys == suppressed_keys:
            return
        for key in self._suppressed_keys - suppressed_keys:
            self._ungrab_key(KEY_TO_KEYCODE[key])
            self._suppressed_keys.remove(key)
        for key in suppressed_keys - self._suppressed_keys:
            self._grab_key(KEY_TO_KEYCODE[key])
            self._suppressed_keys.add(key)
        assert self._suppressed_keys == suppressed_keys
        self._display.sync()
