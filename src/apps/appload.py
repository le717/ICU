# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


from src.registry.registry import Registry
registry = Registry()


def getAllStrings():
    for key in registry.keyNames:
        yield (key, registry.readKey(key, True))
