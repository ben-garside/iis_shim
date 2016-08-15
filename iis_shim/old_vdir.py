# from .helper import _get_property, run
from iis_shim.handler import run, _get_property
from iis_shim.config import *


class VdirsObject():
    def __init__(self):
        pass
    def _get_vdirs(self):
        vdirs = _get_property(APP_CMD, 'VDIR')
        return list(map(VdirObject, vdirs))
    @property
    def list(self):
        return self._get_vdirs()
    @property
    def length(self):
        return len(self._get_vdirs())
    
    def find_by_name(self, name, partial=True):
        """returns array of matched pools"""
        match = []
        for vdir in self._get_vdirs():
            if partial:
                if name.lower() in vdir.name.lower():
                    match.append(vdir)
            else:
                if name.lower() == vdir.name.lower():
                    match.append(vdir)
        return match

class VdirObject():
    def __init__(self, vdirDict):
        self.name = vdirDict['VDIR.NAME']
        self.path = vdirDict['path']
        self.physicalPath = vdirDict['physicalPath']
    
    def set(self):
        pass

    def delete(self):
        pass

    def add(self):
        pass

    def __repr__(self):
        return self.name

Vdirs = VdirsObject()