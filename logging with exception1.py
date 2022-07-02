import logging

logging.basicConfig(filename='logging with exception1.log', level=logging.DEBUG, format='%(levelname)s %(asctime)s %(name)s : %(message)s')

def divide(a, b):
    logging.info(intermediate_var)
    logging.info("The number given by user is  %s and %s", a, b)
    try:
        logging.info('we are into the function')
        div = a / b
        logging.info('division operation completed, The result of the code is %s', div)
        return div
    except Exception as e:
        ##logging.error(e)
        logging.exception(e)

star = '*'
intermediate_var = star * 50
print((divide(3, 9)))
print((divide(3,0)))
