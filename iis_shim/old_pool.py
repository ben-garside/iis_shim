import os
from iis_shim.handler import run, _get_property
# from .helper import _get_property, run
# from .wp import Wps
from iis_shim.config import *

class PoolsObject():
    def __init__(self):
        pass
    def _get_pools(self):
        pools = _get_property(APP_CMD, 'APPPOOL')
        return list(map(PoolObject, pools))
    @property
    def list(self):
        return self._get_pools()

    @property
    def length(self):
        return len(self._get_pools())

    def find_by_name(self, name, partial=True):
        """returns array of matched pools"""
        match = []
        for pool in self._get_pools():
            if partial:
                if name.lower() in pool.name.lower():
                    match.append(pool)
            else:
                if name.lower() == pool.name.lower():
                    match.append(pool)
        return match

class PoolObject():
    def __init__(self, poolDict):
        self.name = poolDict['APPPOOL.NAME']
        self.state = poolDict['state']
        self.runtimeVersion = poolDict['RuntimeVersion']
        self.pipelineMode = poolDict['PipelineMode']
    
    def _refresh(self):
        target = 'APPPOOL /name:"{}"'.format(self.name)
        pool = _get_property(APP_CMD, target)[0]

        self.name = pool['APPPOOL.NAME']
        self.state = pool['state']
        self.runtimeVersion = pool['RuntimeVersion']
        self.pipelineMode = pool['PipelineMode']

    def start(self):
        cmd = '{} START APPPOOL "{}"'.format(APP_CMD, self.name)
        result = run(cmd)
        self._refresh()
        return result
    
    def stop(self):
        cmd = '{} STOP APPPOOL "{}"'.format(APP_CMD, self.name)
        result = run(cmd)
        self._refresh()
        return result
    
    def recycle(self):
        cmd = '{} RECYCLE APPPOOL "{}"'.format(APP_CMD, self.name)
        result = run(cmd)
        self._refresh()
        return result
    
    def add(self):
        pass
    
    def delete(self):
        pass
    
    def set(self):
        pass
    
    def wp(self):
        return Wps.find_by_poolname(self.name, partial=False)[0]

    def __repr__(self):
        return self.state + ' ' + self.name

Pools = PoolsObject()