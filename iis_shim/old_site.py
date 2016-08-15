import logging
from iis_shim.config import *
from iis_shim.handler import run, _get_property

logger = logging.getLogger(__name__)

class SitesObject():
    def __init__(self):
        logger.debug("Created SitesObject")
        self._list = []
        self._list = self.g
        pass
    def _get_sites(self):
        logger.debug("getting sites from IIS")
        sites = _get_property(APP_CMD, 'SITE')
        site_list = list(map(SiteObject, sites))
        logger.debug("Finished fetching sites from IIS")
        return site_list
    @property
    def list(self):
        # return self._get_sites()
        return self._list # this only gets the site once, helps with optimization
    @property
    def length(self):
        return len(self._get_sites())
    def find_by_id(self, id):
        """returns single site or None"""
        for site in self._get_sites():
            if str(id) == site.id:
                return site
        return None
    def find_by_name(self, name, partial=True):
        """returns array of matched sites"""
        match = []
        for site in self._get_sites():
            if partial:
                if name.lower() in site.name.lower():
                    match.append(site)
            else:
                if name.lower() == site.name.lower():
                    match.append(site)
        return match
    def find_by_state(self, state):
        match = []
        for site in self._get_sites():
            if state.lower() == site.state.lower():
                match.append(site)
        return match
    def find_by_binding(self, binding, partial=True):
        match = []
        for site in self._get_sites():
            if partial:
                if binding.lower() in site.binding.lower():
                    match.append(site)
            else:
                if binding.lower() == site.binding.lower():
                    match.append(site)
        return match

class SiteObject():
    def __init__(self, siteDict):
        self._id = siteDict['SITE.ID']
        self._state = siteDict['state']
        self._name = siteDict['SITE.NAME']
        self._binding = siteDict['bindings']
        logger.debug("Found Site: {} - {}".format(self._id, self._name))

    @property
    def id(self):
        self._refresh(prop="name", val=self._name)
        return self._id
    @property
    def name(self):
        self._refresh(prop="id", val=self._id)
        return self._name
    @property
    def state(self):
        self._refresh()
        return self._state
    @property
    def binding(self):
        self._refresh()
        return self._binding

    def _refresh(self, prop=None, val=None):
        prop = prop or "id"
        val = val or self.id
        query = "SITE /{}:{}".format(prop, val)
        site = _get_property(APP_CMD, query)[0]
        self.id = site['SITE.ID']
        self.state = site['state']
        self.name = site['SITE.NAME']
        self.binding = site['bindings']
        logger.info("Refreshed Site: {} - {}".format(self.id, self.name))
        
    def _refreshs(self):
        target = 'SITE /name:"{}"'.format(self.name)
        site = _get_property(APP_CMD, target)[0]
        self.id = site['SITE.ID']
        self.state = site['state']
        self.name = site['SITE.NAME']
        self.binding = site['bindings']
        logger.info("refreshed Site Object")

    def __repr__(self):
        return self.id + ' ' + self.name

    def stop(self):
        cmd = '{} STOP SITE "{}"'.format(APP_CMD, self.name)
        result = run(cmd)
        self._refresh()
        logger.info("Stopped: {}".format(self.name))
        logger.info("State: {} for {}".format(self.state, self.name))
        return result
    
    def start(self):
        cmd = '{} START SITE "{}"'.format(APP_CMD, self.name)
        result = run(cmd)
        self._refresh()
        logger.info("Started: {}".format(self.name))
        logger.info("State: {} for {}".format(self.state, self.name))
        return result
    
    def set(self, prop):
        pass

    def app(self):
        pass

Sites = SitesObject()