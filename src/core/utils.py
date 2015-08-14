# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import ctypes
import logging
import subprocess

__all__ = ("Utils")


class Utils:

    """Utility functions.

    Contains utility functions, including:
    * Reloading with administrator rights

    Exposes the following public properties and methods:
    * runAsAdmin {Method} Tests for and prompts to reload
        with administrator rights.
    """

    @staticmethod
    def runAsAdmin():
        """Check for and reload with administrator rights.

        @returns {?Boolean} True if already running with
                            administrator rights, or the user
                            does not want to reload the program.
        """
        # The program is already being run with admin rights
        if ctypes.windll.shell32.IsUserAnAdmin() == 1:
            return True

        # Reload app
        logging.info("Reloading using RunAsAdmin")
        logging.shutdown()
        subprocess.call("RunAsAdmin.exe")
        raise SystemExit(0)
