import sys


KEYBOARDCONTROL_NOT_FOUND_FOR_OS = \
        "No keyboard control module was found for os %s" % sys.platform

if sys.platform.startswith('linux'):
    from plover_keyboardplus import xkeyboardcontrol as keyboardcontrol
else:
    raise Exception(KEYBOARDCONTROL_NOT_FOUND_FOR_OS)


class KeyboardPlusCapture(keyboardcontrol.KeyboardPlusCapture):
    """Listen to keyboard events."""

    # Supported keys.
    SUPPORTED_KEYS_LAYOUT = '''
    Escape  F1 F2 F3 F4  F5 F6 F7 F8  F9 F10 F11 F12
            F13 F14 F15 F16 F17 F18 F19 F20 F21 F22 F23 F23
      `  1  2  3  4  5  6  7  8  9  0  -  =  \\ BackSpace  Insert Home Page_Up
     Tab  q  w  e  r  t  y  u  i  o  p  [  ]               Delete End  Page_Down
           a  s  d  f  g  h  j  k  l  ;  '      Return
            z  x  c  v  b  n  m  ,  .  /                          Up
                     space                                   Left Down Right
    '''
    SUPPORTED_KEYS = tuple(SUPPORTED_KEYS_LAYOUT.split())

