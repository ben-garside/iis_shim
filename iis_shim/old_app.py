import os
from iis_shim.handler import run, _get_property
from iis_shim.config import *
# from .helper import _get_property
from iis_shim.pool import Pools
# from .pool import Pools
# from .site import Sites
# from .vdir import Vdirs


class AppsObject():
    def __init__(self):
        pass
    def _get_apps(self):
        apps = _get_property(APP_CMD, 'APP')
        return list(map(AppObject, apps))
    # @property
    def list(self):
        return self._get_apps()
    # @property
    def length(self):
        return len(self._get_apps())

    def find_by_name(self, name, partial=True):
        """returns array of matched apps"""
        match = []
        for app in self._get_apps():
            if partial:
                if name.lower() in app.name.lower():
                    match.append(app)
            else:
                if name.lower() == app.name.lower():
                    match.append(app)
        return match
    
    def find_by_sitename(self, name, partial=True):
        """returns array of matched apps"""
        match = []
        for app in self._get_apps():
            if partial:
                if name.lower() in app.siteName.lower():
                    match.append(app)
            else:
                if name.lower() == app.siteName.lower():
                    match.append(app)
        return match
    
    def find_by_poolname(self, name, partial=True):
        """returns array of matched apps"""
        match = []
        for app in self._get_apps():
            if partial:
                if name.lower() in app.poolName.lower():
                    match.append(app)
            else:
                if name.lower() == app.poolName.lower():
                    match.append(app)
        return match

class AppObject():
    def __init__(self, appDict):
        self.path = appDict['path']
        self.name = appDict['APP.NAME']
        self.poolName = appDict['APPPOOL.NAME']
        self.siteName = appDict['SITE.NAME']
    
    def _refresh(self):
        target = 'APP /name:"{}"'.format(self.name)
        app = _get_property(APP_CMD, target)[0]
        self.path = app['path']
        self.name = app['APP.NAME']
        self.poolName = app['APPPOOL.NAME']
        self.siteName = app['SITE.NAME']

    def set(self, prop):
        pass
    
    def delete(self):
        pass
    
    def add(self, appDict):
        pass

    def pool(self):
        return Pools.find_by_name(self.poolName, partial=False)[0]
    

    def site(self):
        return Sites.find_by_name(self.siteName, partial=False)[0]
    

    def vdir(self):
        return Vdirs.find_by_name(self.name, partial=False)[0]
    
    def __repr__(self):
        return self.name

Apps = AppsObject()