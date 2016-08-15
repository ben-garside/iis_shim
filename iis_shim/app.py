from iis_shim.helper import lists, action
import logging

log = logging.getLogger(__name__)

def get_all():
    """ return all app
    """
    apps = lists("APP")
    return apps

def get_by_name(name, partial=False):
    """ return app by name, if partial is true
        a list of apps is returned otherwise a single app
    """
    if not partial:
        app = lists('APP /app.name:"{}"'.format(name))
        if len(app):
            return app[0]
        else:
            return None
    else:
        apps = lists("APP")
        match_apps = [pool for pool in apps if pool['APP.NAME'].lower().find(name.lower()) > -1]
        return match_apps

def get_by_site_name(name, partial=False):
    """ return app by site name, if partial is true
        a list of apps is returned otherwise a single app
    """
    if not partial:
        app = lists('APP /site.name:"{}"'.format(name))
        if len(app):
            return app[0]
        else:
            return None
    else:
        apps = lists("APP")
        match_apps = [pool for pool in apps if pool['APP.NAME'].lower().find(name.lower()) > -1]
        return match_apps

def get_by_pool_name(name, partial=False):
    """ return app by apppool name, if partial is true
        a list of apps is returned otherwise a single app
    """
    if not partial:
        app = lists('APP /apppool.name:"{}"'.format(name))
        if len(app):
            return app[0]
        else:
            return None
    else:
        apps = lists("APP")
        match_apps = [pool for pool in apps if pool['APP.NAME'].lower().find(name.lower()) > -1]
        return match_apps

def get_by_site_name(name, partial=False):
    """ return app by site name, if partial is true
        a list of apps is returned otherwise a single app
    """
    if not partial:
        app = lists('APP /site.name:"{}"'.format(name))
        if len(app):
            return app[0]
        else:
            return None
    else:
        apps = lists("APP")
        match_apps = [pool for pool in apps if pool['SITE.NAME'].lower().find(name.lower()) > -1]
        return match_apps

def length():
    """ return number of pools """
    return len(get_all())