# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import os
import sys
import ctypes
import logging
import platform
import subprocess

from src import constants as const

__all__ = ("Utils")


class Utils:

    """Utility functions.

    Contains utility functions, including:
    * Logging initialization
    * Reloading with administrator rights

    Exposes the following public properties and methods:
    * runAsAdmin {Method} Tests for and prompts to reload
        with administrator rights.
    """

    def __init__(self):
        """Initalize public properties and run utility functions."""
        # Define the log location
        path = os.path.join(os.path.expandvars("%AppData%"),
                            const.CREATOR, const.APP_NAME)
        loggingFile = os.path.join(path, "{0}.log".format(const.APP_NAME))
        if not os.path.exists(path):
            os.makedirs(path)

        # Check if Python is x86
        pythonArch = "x64"
        if sys.maxsize < 2 ** 32:
            pythonArch = "x86"

        logging.basicConfig(
            level=logging.DEBUG,
            format="%(asctime)s : %(levelname)s : %(message)s",
            filename=loggingFile,
            filemode="a"
        )

        logging.info("Begin logging to {0}".format(loggingFile))
        logging.info("You are running {0} {1} {2} on {3} {4}.".format(
                     platform.python_implementation(),
                     pythonArch,
                     platform.python_version(),
                     platform.machine(),
                     platform.platform())
                     )
        logging.info("""
#########################################
{0} v{1}
Created 2015 {2}

If you run into a bug, open an issue at
https://github.com/le717/{0}/issues
and attach this file for an quicker fix!
#########################################
                                    """.format(const.APP_NAME, const.VERSION,
                                               const.CREATOR))
        return True

    def runAsAdmin(self):
        """Check for and reload with administrator rights.

        @returns {?Boolean} False if already running with
                            administrator rights, or the user
                            does not want to reload the program.
        """
        # The program is already being run with admin rights
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            return False

        # Reload app
        logging.info("Reloading using RunAsAdmin")
        logging.shutdown()
        subprocess.call("RunAsAdmin.exe")
        raise SystemExit(0)
