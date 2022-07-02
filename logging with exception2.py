import logging
logging.basicConfig(filename='logging with exception2.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s : %(message)s')

try:
    logging.info("we are trying to read the file")
    with open("karthik.txt", "r"):
        logging.info("user successfully read the file")
except Exception as e:
    logging.critical("This is critical situation")
    logging.error(e)
    logging.exception(e)
