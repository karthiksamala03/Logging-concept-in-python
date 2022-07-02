import logging

logging.basicConfig(filename='logging info of diff users.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s : %(message)s')

# Create Handlers
consol_log = logging.StreamHandler()
consol_log.setLevel(logging.DEBUG)
format = logging.Formatter('%(levelname)s %(asctime)s %(name)s : %(message)s')
consol_log.setFormatter(format)

# Creating a Custom Logger
logging.getLogger().addHandler(consol_log)
logging.info("user Root -  main log")
logger1 = logging.getLogger('User1')
logger2 = logging.getLogger('User2')
logger1.info("This is info for USER1")
logger1.debug("This is debug for USER1")
logger2.info("This is info for USER2")

