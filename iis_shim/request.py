# from .helper import _get_property, run
from iis_shim.handler import run, _get_property
from iis_shim.config import *

class RequestsObject():
    def __init__(self):
        pass
    def _get_requests(self):
        requests = _get_property(APP_CMD, 'REQUESTS')
        return list(map(RequestObject, requests))
    @property
    def list(self):
        return self._get_requests()
    @property
    def length(self):
        return len(self._get_requests())

class RequestObject():
    def __init__(self, rDict):
        self.name = rDict['REQUEST.NAME']
        self.clientIp = rDict['ClientIp']
        self.wp = rDict['WP.NAME']
        self.url = rDict['Url']
        self.time = rDict['Time']
        self.stage =rDict['Stage']
        self.siteId = rDict['SITE.ID']
        self.apppool = rDict['APPPOOL.NAME']
        self.verb = rDict['Verb']
        self.module = rDict['Module']
    
    def __repr__(self):
        return self.name + ' ' + self.apppool
    
    def data(self):
        return {
            'name': self.name,
            'clientIp': self.clientIp,
            'wp': self.wp,
            'url': self.url,
            'time': self.time,
            'stage': self.stage,
            'siteId': self.siteId,
            'apppool': self.apppool,
            'verb': self.verb,
            'module': self.module
        }