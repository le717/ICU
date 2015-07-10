# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


from src.core.queue import ActionsQueue


class Responses:

    def __init__(self, ICU):
        self.makeAction = ICU.makeAction
        self.queue = ActionsQueue(ICU.firstLoad)

    # Mass actions
    def actionApply(self, val):
        print("", val)

    def actionReset(self):
        print("reset")
        self.queue.clear()

    # Normal buttons
    def btnBrowse(self, val):
        print("", val)

    def btnRedirect(self, val):
        print("", val)

    # Radio buttons
    def radioColor256(self, val):
        print("color", "8")
        self.queue.add(self.makeAction("color", "8"))

    def radioColor16b(self, val):
        print("color", "16")
        self.queue.add(self.makeAction("color", "16"))

    def radioModelLow(self, val):
        print("model", "0")
        self.queue.add(self.makeAction("model", "0"))

    def radioModelFast(self, val):
        print("model", "1")
        self.queue.add(self.makeAction("model", "1"))

    def radioModelHigh(self, val):
        print("model", "2")
        self.queue.add(self.makeAction("model", "2"))

    def radioTexFast(self, val):
        print("texture", "0")
        self.queue.add(self.makeAction("texture", "0"))

    def radioTexHigh(self, val):
        print("texture", "1")
        self.queue.add(self.makeAction("texture", "1"))

    # Check boxes
    def chkCursor(self, val):
        print("cursor", val)
        self.queue.add(self.makeAction("cursor", val))

    def chkDraw3D(self, val):
        print("draw3d", val)
        self.queue.add(self.makeAction("draw3d", val))

    def chkFlipSurface(self, val):
        print("surface", val)
        self.queue.add(self.makeAction("surface", val))

    def chkWindowed(self, val):
        print("windowed", not val)
        self.queue.add(self.makeAction("windowed", not val))

    def chkJoystick(self, val):
        print("joystick", val)
        self.queue.add(self.makeAction("joystick", val))

    def chkMusic(self, val):
        print("music", val)
        self.queue.add(self.makeAction("music", val))

    def chkSound(self, val):
        print("sound", val)
        self.queue.add(self.makeAction("sound", val))

    def chkWideAngle(self, val):
        print("wideangle", val)
        self.queue.add(self.makeAction("wideangle", val))

    # Direct3D dropdown selection
    def comboD3D(self, val):
        print("d3d", val)
        self.queue.add(self.makeAction("d3d", val))
