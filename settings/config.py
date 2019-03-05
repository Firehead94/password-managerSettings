from sys import platform
import os




DEFAULT_LOCAL_PATH_WINDOWS = os.getenv('APPDATA') + "\\VisualSP2019"
DEFAULT_LOCAL_PATH_MAC = "~/Library/Preferences/visualsp"
DEFAULT_LOCAL_PATH_LINUX = "~/.visualsp/"
DEFAULT_LOCAL_PATH_DEFAULT = ""

DEFAULT_USER_FOLDER = "\\users"
DEFAULT_CAMERA_FOLDER = "\\video"
DEFAULT_MISC_FOLDER = "\\misc"

DEFAULT_ACCESS_LEVEL = "0"
GENERAL_ACCESS_LEVEL = "0"
ADMIN_ACCESS_LEVEL = "10"

osType = "Default"
storage = dict(
    pathW = DEFAULT_LOCAL_PATH_WINDOWS,
    pathM = DEFAULT_LOCAL_PATH_MAC,
    pathL = DEFAULT_LOCAL_PATH_LINUX,
    pathDefault = DEFAULT_LOCAL_PATH_DEFAULT
)



if platform == "linux":
    osType = "L"
elif platform == "darwin":
    osType == "M"
elif platform == "win32" or platform == "win64":
    osType = "W"

folderVideo = storage["path" + osType] + DEFAULT_CAMERA_FOLDER
folderUser = storage["path" + osType] + DEFAULT_USER_FOLDER
if not os.path.exists(folderVideo):
    os.makedirs(folderVideo)

if not os.path.exists(folderUser):
     os.makedirs(folderUser)

