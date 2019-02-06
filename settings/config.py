from sys import platform

DEFAULT_LOCAL_PATH_WINDOWS = "%appdata%/VisualSP2019/Users/"
DEFAULT_LOCAL_PATH_MAC = "~/Library/Preferences"
DEFAULT_LOCAL_PATH_LINUX = "~/.visualsp"

DEFAULT_ACCESS_LEVEL = "0"
GENERAL_ACCESS_LEVEL = "0"
ADMIN_ACCESS_LEVEL = "10"

osType = "W"
storage = dict(
    pathW=DEFAULT_LOCAL_PATH_WINDOWS,
    pathM=DEFAULT_LOCAL_PATH_MAC,
    pathL=DEFAULT_LOCAL_PATH_LINUX,
)


def __init__(self):
    if platform == "linux":
        self.osType = "L"
    elif platform == "darwin":
        self.osType == "M"
    elif platform == "win32" or platform == "win64":
        self.osType = "W"
