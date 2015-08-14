# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


from src.core.utils import Utils
from src.registry.registry import Registry
from src.ui.responses import Responses


class ICU:

    def __init__(self):
        registry = Registry()
        self.firstLoad = []
        self._rmap = {}
        self._map = {
            "3D Device Name": "d3d",
            "3DSound": "sound",
            "Back Buffers in Video RAM": "draw3d",
            "Display Bit Depth": "color",
            "Draw Cursor": "cursor",
            "Flip Surfaces": "surface",
            "Full Screen": "windowed",
            "Island Quality": "model",
            "Island Texture": "texture",
            "Music": "music",
            "savepath": "savepath",
            "UseJoystick": "joystick",
            "Wide View Angle": "wideangle"
        }

        # Create a reverse conversion map
        for k, v in self._map.items():
            self._rmap[v] = k

        # Get the initial registry values
        for key in registry.readAll():
            self.firstLoad.append(
                Utils.makeAction(self.convertKeyNames(key[0]), key[1])
            )

        # Connect the buttons to the queue
        self.responses = Responses(self)

    def convertKeyNames(self, name):
        if name in self._map:
            return self._map[name]
        elif name in self._rmap:
            return self._rmap[name]
