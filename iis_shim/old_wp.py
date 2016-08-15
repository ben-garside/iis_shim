from iis_shim.handler import run, _get_property
from iis_shim.config import *

class WorkerProcessorsObject():
    def __init__(self):
        pass
    def _get_wps(self):
        wps = _get_property(APP_CMD, 'WP')
        return list(map(WorkerProcessorObject, wps))
    @property
    def list(self):
        return self._get_wps()
    @property
    def length(self):
        return len(self._get_wps())
    
    def find_by_poolname(self, name, partial=True):
        """returns array of matched wps"""
        match = []
        for wp in self._get_wps():
            if partial:
                if name.lower() in wp.apppool.lower():
                    match.append(wp)
            else:
                if name.lower() == wp.apppool.lower():
                    match.append(wp)
        return match

class WorkerProcessorObject():
    def __init__(self, wpDict):
        self.name = wpDict['WP.NAME']
        self.apppool = wpDict['APPPOOL.NAME']
    
    def __repr__(self):
        return self.name + ' ' + self.apppool

Wps = WorkerProcessorsObject()