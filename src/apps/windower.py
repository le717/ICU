# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


from src.registry.registry import Registry

__all__ = ("Windower")


class Windower:

    def __init__(self, shouldEnable):
        self.registry = Registry()
        if shouldEnable:
            self.__enable()
        else:
            self.__disable()

    def __enable(self):
        self.registry.writeKey("3D Device Name", "Ramp Emulation")
        self.registry.writeKey("Full Screen", False, True)
        self.registry.writeKey("Back Buffers in Video RAM", False, True)
        self.registry.writeKey("Flip Surfaces", False, True)
        return True

    def __disable(self):
        self.registry.writeKey("Full Screen", True, True)
        return True
