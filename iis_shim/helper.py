from iis_shim.handler import run
from iis_shim.config import APP_CMD
import xml.etree.cElementTree as ET
import logging

log = logging.getLogger(__name__)

def lists(action, style="/XML", processXml=True):
    cmd = "{} LIST {} {}".format(APP_CMD, action, style)
    output = run(cmd)
    if processXml:
        output = process_xml(output)
    return output

def action(action, prop, name, style="/XML", processXml=True):
    cmd = '{} {} {} "{}" {}'.format(APP_CMD, action, prop, name, style)
    output = run(cmd)
    if processXml:
        output = process_xml(output)
    return output

def process_xml(xmlString):
    if xmlString.endswith("None"):
        xmlString = xmlString[:-4]
    try:
        tree = ET.fromstring(xmlString)
        splitResult = [item.attrib for item in tree if len(item.attrib) > 0]
        log.debug("found {} items in processed xml".format(len(splitResult)))
        return splitResult
    except (Exception) as e:
        log.error("found exception in process_xml {}".format(str(e)))