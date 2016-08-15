from iis_shim.helper import lists, process_xml
# from iis_shim._site import *
import iis_shim as iis
# from iis_shim.app import Apps
# import iis_shim as iis

# sites = lists("Site", processXml=True)
iis.pool.stop_by_id(1)
iis.pool.get_by_name("pool", partial=True)
print('x')
