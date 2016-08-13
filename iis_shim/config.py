import os
osDrive = os.getenv("SYSTEMDRIVE")
IIS_ROOT = "{}\\Windows\\System32\\inetsrv".format(osDrive)
APP_CMD = "{}\\appcmd.exe".format(IIS_ROOT)