from win32 import path
path.add_parent(__file__, levels=1)

from iis_shim import helper

sites = helper.lists("Site")
z = helper.process_xml("<xml>lmkdnd</xml>")
print('x')