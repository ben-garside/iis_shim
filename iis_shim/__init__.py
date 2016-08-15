import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# loggerHandler = logging.StreamHandler(stream=sys.stdout)
# loggerHandler.setLevel(logging.DEBUG)
# loggerFormatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
# loggerHandler.setFormatter(loggerFormatter)

# logger.addHandler(loggerHandler)

import iis_shim.site as site 
import iis_shim.pool as pool
import iis_shim.app as app
import iis_shim.vdir as vdirs
import iis_shim.wp as wps

apppool = pool
app_pool = pool