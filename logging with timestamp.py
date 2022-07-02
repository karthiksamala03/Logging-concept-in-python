import logging

logging.basicConfig(filename='logging with timestamp.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s %(message)s')
logging.info('This is info with timestamp')