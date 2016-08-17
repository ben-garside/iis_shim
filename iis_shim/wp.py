from iis_shim.helper import lists, action
import logging

log = logging.getLogger(__name__)

def get_all():
    """ return all vdirs
    """
    vdirs = lists("WPS")
    return vdirs

def get_by_name(name):
    """ return wp by name
        return a single wp
    """
    vdir = lists('WPS /wp.name:"{}"'.format(name))
    if len(vdir):
        return vdir[0]
    else:
        return None

def get_by_pool_name(name, partial=False):
    """ return wp by apppool name, if partial is true
        a list of wps is returned otherwise a single wp
    """
    if not partial:
        vdir = lists('WPS /apppool.name:"{}"'.format(name))
        if len(vdir):
            return vdir[0]
        else:
            return None
    else:
        vdirs = lists("WPS")
        match_vdirs = [vdir for vdir in vdirs if vdir['APPPOOL.NAME'].lower().find(name.lower()) > -1]
        return match_vdirs

def length():
    """ return number of pools """
    return len(get_all())
