import sys
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

loggerHandler = logging.StreamHandler(stream=sys.stdout)
loggerHandler.setLevel(logging.DEBUG)
loggerFormatter = logging.Formatter('%(levelname)s:%(name)s: %(message)s')
loggerHandler.setFormatter(loggerFormatter)

logger.addHandler(loggerHandler)