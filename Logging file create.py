import logging
logging.basicConfig(filename='demo.log', level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('This is demo log in file')
logging.warning('This is warning msg')
logging.error('This is for error')

