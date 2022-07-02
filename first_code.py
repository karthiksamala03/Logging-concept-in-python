import logging
logging.basicConfig(filename="first_code.log", level=logging.INFO)
logging.info("This is my first logging code")

l = [1,2,3,4,5]

for i in l:
    if i == 2:
        logging.info(l)
logging.shutdown()
logging.info("This is info logging code")
logging.warning("This is a warning message")
logging.error("This is a error message")
logging.critical("This is a critical message")