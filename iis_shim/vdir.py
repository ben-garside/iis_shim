from iis_shim.helper import lists, action
import iis_shim.site as sites
import iis_shim.app as apps
import logging

log = logging.getLogger(__name__)

def get_all():
    """ return all vdirs
    """
    vdirs = lists("APVDIR")
    return vdirs

def get_by_name(name, partial=False):
    """ return vdir by name, if partial is true
        a list of vdirs is returned otherwise a single vdir
    """
    if not partial:
        vdir = lists('VDIR /name:"{}"'.format(name))
        if len(vdir):
            return vdir[0]
        else:
            return None
    else:
        vdirs = lists("VDIR")
        match_vdirs = [vdir for vdir in vdirs if vdir['VDIR.NAME'].lower().find(name.lower()) > -1]
        return match_vdirs

def get_by_physicalpath(name, partial=False):
    """ return vdir by physicalpath, if partial is true
        a list of vdirs is returned otherwise a single vdir
    """
    if not partial:
        vdir = lists('VDIR /physicalpath:"{}"'.format(name))
        if len(vdir):
            return vdir[0]
        else:
            return None
    else:
        vdirs = lists("VDIR")
        match_vdirs = [vdir for vdir in vdirs if vdir['physicalPath'].lower().find(name.lower()) > -1]
        return match_vdirs

def get_by_path(name, partial=False):
    """ return vdir by path, if partial is true
        a list of vdirs is returned otherwise a single vdir
    """
    if not partial:
        vdir = lists('VDIR /path:"{}"'.format(name))
        if len(vdir):
            return vdir[0]
        else:
            return None
    else:
        vdirs = lists("VDIR")
        match_vdirs = [vdir for vdir in vdirs if vdir['path'].lower().find(name.lower()) > -1]
        return match_vdirs

def get_by_app_name(name, partial=False):
    """ return vdir by name, if partial is true
        a list of vdirs is returned otherwise a single vdir
    """
    if not partial:
        vdir = lists('VDIR /APP.NAME:"{}"'.format(name))
        if len(vdir):
            return vdir[0]
        else:
            return None
    else:
        vdirs = lists("VDIR")
        match_vdirs = [vdir for vdir in vdirs if vdir['APP.NAME'].lower().find(name.lower()) > -1]
        return match_vdirs

def get_by_site_id(id):
    site = sites.get_by_id(id)
    if site:
        app = apps.get_by_site_name(site['SITE.NAME'])
        if app:
            vdir = get_by_app_name(app['APP.NAME'])
            if vdir:
                return vdir
    return None

def length():
    """ return number of pools """
    return len(get_all())