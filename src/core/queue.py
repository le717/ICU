# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


class ActionsQueue:

    def __init__(self):
        self.queue = []


class Responses:

    def __init__(self):
        pass

    # Normal buttons
    def btnBrowse(self, val):
        print(val)

    def actionReset(self, val):
        print(val)

    def btnRedirect(self, val):
        print(val)

    # Radio buttons
    def radioColor256(self, val):
        print(val)

    def radioColor16b(self, val):
        print(val)

    def radioModelLow(self, val):
        print(val)

    def radioModelFast(self, val):
        print(val)

    def radioModelHigh(self, val):
        print(val)

    def radioTexFast(self, val):
        print(val)

    def radioTexHigh(self, val):
        print(val)

    # Check boxes
    def chkCursor(self, val):
        print(val)

    def chkDraw3D(self, val):
        print(val)

    def chkFlipVideo(self, val):
        print(val)

    def chkFullscreen(self, val):
        print(val)

    def chkJoystick(self, val):
        print(val)

    def chkMusic(self, val):
        print(val)

    def chkSound(self, val):
        print(val)

    # Direct3D dropdown selection
    def comboD3D(self, val):
        print(val)
