# -*- coding: utf-8 -*-
"""ICU (LEGO Island Configuration Utility).

Created 2015 Triangle717
<http://le717.github.io/>

Licensed under The MIT License
<http://opensource.org/licenses/MIT/>

"""


import winreg
import platform


__all__ = ("Registry")


class Registry:

    def __init__(self):
        self.folPath = ("SOFTWARE\Wow6432Node\Mindscape\LEGO Island"
                        if platform.machine() == "AMD64"
                        else "SOFTWARE\Mindscape\LEGO Island")
        self.keyNames = ("3D Device Name", "3DSound",
                         "Back Buffers in Video RAM", "Display Bit Depth",
                         "Draw Cursor", "Flip Surfaces", "Full Screen",
                         "Island Quality", "Island Texture",
                         "Music", "savepath", "UseJoystick",
                         "Wide View Angle")
        self.otherKeyNames = ("diskpath", "JoystickIndex", "moviespath")

    @staticmethod
    def __convertBool(val):
        """Convert boolean values between Python and the game.

        @param {Boolean|String} val Boolean value to convert.
                                    String values of YES or NO
                                    are converted to True or False,
                                    and vice-versa for Boolean values.
        @return {Boolean|String}
        """
        if type(val) == str:
            val = (True if val == "YES" else False)
        elif type(val) == bool:
            val = ("YES" if val else "NO")
        return val

    def __validateKeyName(self, key):
        """Ensure the given registry key name is valid.

        @param {String} key Key name to validate.
        @return {!Boolean} True if valid, KeyError thrown otherwise.
        """
        if key in self.keyNames:
            return True
        raise KeyError("Key '{0}' is not a valid registry entry!".format(
                       key))

    def readKey(self, key, convertBool=False):
        """Read a configuration key.

        @param {String} key Valid registry key name.
        @param {Boolean} [convertBool=False] Convert boolean values between
                                             Python and game versions.
        @return {Boolean|String} Value of the key requested,
                                 Boolean version if convertBool = True.
        """
        if self.__validateKeyName(key):
            with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, self.folPath) as r:
                val = winreg.QueryValueEx(r, key)[0]

            # Convert any boolean values
            if convertBool:
                val = self.__convertBool(val)
            return val

    def writeKey(self, key, val, convertBool=False):
        """Write a configuration key.

        @param {String} key Valid registry key name.
        @param {String} val The new value of the specified key.
        @param {Boolean} [convertBool=False] Convert boolean values between
                                             Python and game versions.
        @return {Boolean|String} Value of the key requested,
                                 Boolean version if convertBool = True.
        """
        if self.__validateKeyName(key):
            # Convert any boolean values
            if convertBool:
                val = self.__convertBool(val)

            with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE,
                                    self.folPath) as r:
                winreg.SetValueEx(r, key, 0, winreg.REG_SZ, val)
            return True
