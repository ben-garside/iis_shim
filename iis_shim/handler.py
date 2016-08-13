import subprocess
import xml.etree.cElementTree as ET
import os
import logging

logger = logging.getLogger(__name__)

def run(cmd, errMsg=None):
    """ run given commands in a subprocess
    """
    try:
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        output, err = proc.communicate()
        if type(output) == bytes:
            output = output.decode(encoding='UTF-8')
        if "[Error]" in output or proc.returncode != 0:
            if errMsg:
                # raise Exception(errMsg)
                return errMsg
            else:
                return "%s\r\n%s" % (output, err)
        return output
    except Exception:
        return Exception

def _get_property(APP_CMD, prop):
    if os.path.isfile(APP_CMD):
        cmd = "{} LIST {} /XML".format(APP_CMD, prop)
        results = run(cmd)
        try:
            tree = ET.fromstring(results)
        except Exception as e:
            tree = []
            print("expection: {} when parsing below xml: \n {}".format(e, results))
        
        splitResult = [item.attrib for item in tree if len(item.attrib) > 0]
        logger.debug("Found: {} matching Query: {}".format(len(splitResult), prop))
        return splitResult
    else:
        return []