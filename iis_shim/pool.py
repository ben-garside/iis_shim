from iis_shim.helper import lists, action
import iis_shim.site as sites
import iis_shim.app as apps
import logging

log = logging.getLogger(__name__)

def get_all():
    """ return all apppools
    """
    pools = lists("APPPOOL")
    return pools

def get_by_runtimeverion(verion):
    """ return pool by RuntimeVersion
    """
    pool = lists('APPPOOL /RuntimeVersion:"{}"'.format(verion))
    if len(pool):
        return pool[0]
    return None

def get_by_name(name, partial=False):
    """ return pool by name, if partial is true
        a list of pools is returned otherwise a single pool
    """
    if not partial:
        pool = lists('APPPOOL /name:"{}"'.format(name))
        if len(pool):
            return pool[0]
        else:
            return None
    else:
        pools = lists("APPPOOL")
        match_pools = [pool for pool in pools if pool['APPPOOL.NAME'].lower().find(name) > -1]
        return match_pools

def get_by_state(state):
    states = ["started", "stopped"]
    if state.lower() in states:
        pools = lists('APPPOOL /state:"{}"'.format(state.lower()))
        return pools
    else:
        log.error("Invalid state. use 'Started' or 'Stopped'")
        return []

def get_by_PipelineMode(mode):
    modes = ["Integrated", "Classic"]
    if mode.lower() in modes:
        pools = lists('APPPOOL /PipelineMode:"{}"'.format(mode.lower()))
        return pools
    else:
        log.error("Invalid mode. use 'Integrated' or 'Classic'")
        return []

def get_by_site_id(id):
    site = sites.get_by_id(id)
    if site:
        app = apps.get_by_site_name(site['SITE.NAME'])
        if app:
            pool = get_by_name(app['APPPOOL.NAME'])
            if pool:
                return pool
    return None

def stop_by_site_id(id):
    pool = get_by_site_id(id)
    if pool:
        output = action("STOP", "APPPOOL", pool['APPPOOL.NAME'])
        if len(output):
            return output[0]
    return None

def start_by_site_id(id):
    pool = get_by_site_id(id)
    if pool:
        output = action("START", "APPPOOL", pool['APPPOOL.NAME'])
        if len(output):
            return output[0]
    return None

def length():
    """ return number of pools """
    return len(get_all())