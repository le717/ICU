# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import os
import sys
import logging
import platform

from src import constants as const


__all__ = ("Logger")


class Logger:

    """Application logging."""

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
