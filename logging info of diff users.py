import logging

logging.basicConfig(filename='logging info of diff users.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s : %(message)s')

consol_log = logging.StreamHandler()
consol_log.setLevel(logging.INFO)
format = '%(levelname)s %(asctime)s %(name)s : %(message)s'
consol_log.setFormatter(format)
logging.getLogger().addHandler(consol_log)
logging.info("logging of code for multiple users")
logger1 = logging.getLogger('logger1.area1')
logger2 = logging.getLogger('logger2.area2')
logger1.info("This is info for logger1")
logger1.debug("This is debug for logger1")
logger2.info("This is info for logger2")