# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import os
import distutils.file_util
from src.registry.strings import Registry

__all__ = ("ReDirect")


class ReDirect:

    def __init__(self, newPath):
        self.registry = Registry()
        self.curPath = self.registry.readKey("savepath")
        self.newPath = newPath.replace("/", "\\")

        # Make sure the paths are different
        # TODO Display a message
        if self.curPath.lower() == self.newPath.lower():
            return False

        # Make sure the new path exists
        if not os.path.exists(self.newPath):
            os.makedirs(self.newPath)

        # Update the registry key
        self.registry.writeKey("savepath", self.newPath)

        # Move the saves
        for f in self.__findSaves():
            distutils.file_util.move_file(
                os.path.join(self.curPath, f),
                os.path.join(self.newPath, f)
            )

    def __findSaves(self):
        for f in os.listdir(self.curPath):
            fl = f.lower()
            if fl.endswith(".gs") or fl.endswith(".gsi"):
                yield f
