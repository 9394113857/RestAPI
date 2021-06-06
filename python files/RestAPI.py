# RestAPI.py

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler("F:\Restful-API's\RestAPI\log files\RestAPI.log")
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)
"""
name = 'Raghu'
logging.warning('%s raised a warning', name)
"""

logger.info('See the RestAPI.log file')
name = 'Krunal'
logging.warning(' %s raised a warning', name)

name = 'Krunal'
logging.warning(f' {name} raised an warning') # space is executing

logger = logging.getLogger('demo logger')
logger.error(' This is an error')





