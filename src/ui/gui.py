"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QFont, QFontDatabase

from src import constants as const
from src.core.core import ICU
from src.core.logger import Logger
from src.core.utils import Utils
from src.ui import main as mainUi

__all__ = ("GUI")

def callMe(*args):
    print(args)


class GUI:

    """PyQt 5-based GUI for Blocks.

    Provides public access to key visual areas including
        file name and editing area.
    """

    def __init__(self):
        """Setup the GUI."""
        # Check admin rights before anything else
        # utils = Utils()
        # utils.runAsAdmin()
        # Logger()

        self.qApp = QtWidgets.QApplication(sys.argv)
        self.qApp.setStyle("fusion")
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = mainUi.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)

        # Instance the back-end code
        core = ICU()
        self.queue = core.responses

        # Normal buttons
        self.ui.btnApply.clicked.connect(self.queue.actionApply)
        self.ui.btnBrowse.clicked.connect(self.queue.btnBrowse)
        self.ui.btnClose.clicked.connect(self.MainWindow.close)
        self.ui.btnReset.clicked.connect(self.queue.actionReset)
        self.ui.btnRedirect.clicked.connect(self.queue.btnRedirect)

        # Radio buttons
        self.ui.radioColor256.clicked.connect(self.queue.radioColor256)
        self.ui.radioColor16b.clicked.connect(self.queue.radioColor16b)
        self.ui.radioModelLow.clicked.connect(self.queue.radioModelLow)
        self.ui.radioModelFast.clicked.connect(self.queue.radioModelFast)
        self.ui.radioModelHigh.clicked.connect(self.queue.radioModelHigh)
        self.ui.radioTexFast.clicked.connect(self.queue.radioTexFast)
        self.ui.radioTexHigh.clicked.connect(self.queue.radioTexHigh)

        # Check boxes
        self.ui.chkCursor.toggled.connect(self.queue.chkCursor)
        self.ui.chkDraw3D.toggled.connect(self.queue.chkDraw3D)
        self.ui.chkFlipSurface.toggled.connect(self.queue.chkFlipSurface)
        self.ui.chkWindowed.toggled.connect(self.queue.chkWindowed)
        self.ui.chkJoystick.toggled.connect(self.queue.chkJoystick)
        self.ui.chkMusic.toggled.connect(self.queue.chkMusic)
        self.ui.chkSound.toggled.connect(self.queue.chkSound)
        self.ui.chkWideAngle.toggled.connect(self.queue.chkWideAngle)

        # Direct3D dropdown selection
        self.ui.comboD3D.activated["QString"].connect(self.queue.comboD3D)

        # Connect the menu items
        # self.ui.actionAbout.triggered.connect(callMe)
        self.ui.actionApply.triggered.connect(self.queue.actionApply)
        self.ui.actionReset.triggered.connect(self.queue.actionReset)
        self.ui.actionQuit.triggered.connect(self.__quit)

        # Set up and run app
        self.__setDetails()
        self.MainWindow.show()
        self.qApp.exec_()

    def __setDetails(self):
        """Set the program details in the GUI.

        @return {Boolean} Always returns True.
        """
        self.MainWindow.setWindowTitle("{0} {1}".format(
            const.APP_NAME, const.VERSION))
        return True

    def __quit(self):
        logging.shutdown()
        raise SystemExit(0)

#    def __showAboutDialog(self):
#        """Display the About dialog.
#
#        @return {Boolean} Always returns True.
#        """
#        dialogWindow = QtWidgets.QDialog()
#        ui = aboutUi.Ui_aboutDiag()
#        ui.setupUi(dialogWindow)
#        dialogWindow.setWindowTitle(
#            dialogWindow.windowTitle().replace("app-name", const.APP_NAME))
#        ui.lbHeader.setText(
#            ui.lbHeader.text().replace("app-name", const.APP_NAME))
#        ui.lbHeader.setText(
#            ui.lbHeader.text().replace("app-version", const.VERSION))
#        ui.lbCreated.setText(
#            ui.lbCreated.text().replace("app-creator", const.CREATOR))
#        ui.btnGitHub.clicked.connect(
#            lambda: webbrowser.open_new_tab("https://github.com/le717/ICU")
#        )
#        ui.btnLicense.clicked.connect(
#            lambda: webbrowser.open_new_tab(
#                "http://www.gnu.org/licenses/gpl-3.0-standalone.html"))
#        dialogWindow.exec_()
#        return True
