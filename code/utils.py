import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource (for dev and PyInstaller .exe) """
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)