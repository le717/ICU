# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


class Responses:

    def __init__(self):
        pass

    # Mass actions
    def actionApply(self, val):
        print("", val)

    def actionReset(self, val):
        print("", val)

    # Normal buttons
    def btnBrowse(self, val):
        print("", val)

    def btnRedirect(self, val):
        print("", val)

    # Radio buttons
    def radioColor256(self, val):
        print("color", "8")

    def radioColor16b(self, val):
        print("color", "16")

    def radioModelLow(self, val):
        print("model", "0")

    def radioModelFast(self, val):
        print("model", "1")

    def radioModelHigh(self, val):
        print("model", "2")

    def radioTexFast(self, val):
        print("texture", "0")

    def radioTexHigh(self, val):
        print("texture", "1")

    # Check boxes
    def chkCursor(self, val):
        print("cursor", val)

    def chkDraw3D(self, val):
        print("draw3d", val)

    def chkFlipSurface(self, val):
        print("surface", val)

    def chkWindowed(self, val):
        print("windowed", val)

    def chkJoystick(self, val):
        print("joystick", val)

    def chkMusic(self, val):
        print("music", val)

    def chkSound(self, val):
        print("sound", val)

    def chkWideAngle(self, val):
        print("wideangle", val)

    # Direct3D dropdown selection
    def comboD3D(self, val):
        print("d3d", val)