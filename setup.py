# -*- coding: utf-8 -*
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import os
import sys
import subprocess
from cx_Freeze import (setup, Executable)

from src import constants as const
# from Tools.bin import (copyfiles, runasadmin)

# Only compile GUI on full build
if sys.argv[1] == "build":
    print("Generating GUI resources")
    from PyQt5 import uic
    uic.compileUiDir("src/ui")
    subprocess.call(["pyrcc5", "src/ui/graphics.qrc", "-o", "graphics_rc.py"])

if sys.platform == "win32":
    if sys.maxsize < 2 ** 32:
        destFolder = os.path.join("bin", "Windows", "x86")
    else:
        destFolder = os.path.join("bin", "Windows", "x64")

else:
    print("{0} is not supported on non Windows OS!".format(const.APP_NAME))
    raise SystemExit(0)

# Create the freeze path if it doesn't exist
if not os.path.exists(destFolder):
    os.makedirs(destFolder)

# Copy required files
build_exe_options = {
    "build_exe": destFolder,
    "create_shared_zip": True,
    "compressed": True,
    "optimize": 2,
    "icon": "src/ui/images/ICU.ico"
}

setup(
    name=const.APP_NAME,
    version=const.VERSION,
    author=const.CREATOR,
    description=const.APP_NAME,
    license="The MIT License",
    options={"build_exe": build_exe_options},
    executables=[Executable("{0}.py".format(const.APP_NAME),
                 targetName="{0}.exe".format(const.APP_NAME),
                            base="Win32GUI")]
)
