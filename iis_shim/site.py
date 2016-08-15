from iis_shim.helper import lists, action
import logging

log = logging.getLogger(__name__)

def get_all():
    """ return all sites
    """
    sites = lists("Site")
    return sites

def get_by_id(id):
    """ return site by id
    """
    site = lists("Site /id:{}".format(id))
    if len(site):
        return site[0]
    return None

def get_by_name(name, partial=False):
    """ return site by name, if partial is true
        a list of sites is returned otherwise a single site
    """
    if not partial:
        site = lists('Site /name:"{}"'.format(name))
        if len(site):
            return site[0]
        else:
            return None
    else:
        sites = lists("Site")
        match_sites = [site for site in sites if site['SITE.NAME'].lower().find(name) > -1]
        return match_sites

def get_by_state(state):
    states = ["started", "stopped"]
    if state.lower() in states:
        sites = lists('Site /state:"{}"'.format(state.lower()))
        return sites
    else:
        log.error("Invalid state. use 'Started' or 'Stopped'")
        return []
def get_by_bindings(binding, partial=False):
    if not partial:
        site = lists('Site /bindings:"{}"'.format(binding))
        if len(site):
            return site[0]
        else:
            return None
    else:
        sites = lists("Site")
        match_sites = [site for site in sites if site['bindings'].lower().find(binding) > -1]
        return match_sites

def stop_by_id(id):
    site = get_by_id(id)
    if site:
        output = action("STOP", "Site", site['SITE.NAME'])
        if len(output):
            return output[0]
    return None

def start_by_id(id):
    site = get_by_id(id)
    if site:
        output = action("START", "Site", site['SITE.NAME'])
        if len(output):
            return output[0]
    return None

def length():
    """ return number of sites """
    return len(get_all())