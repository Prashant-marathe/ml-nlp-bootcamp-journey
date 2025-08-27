import logging

# configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticApp')
logger.setLevel(logging.DEBUG)


def add(a, b):
    result = a + b
    logger.debug(f'{a} + {b} = {result}')
    return result

def substract(a, b):
    result = a - b
    logger.debug(f'{a} - {b} = {result}')
    return result

def multiply(a, b):
    result = a * b
    logger.debug(f'{a} * {b} = {result}')
    return result

def divide(a, b):
    try: 
        result = a / b
        logger.debug(f'{a} / {b} = {result}')
        return result
    except ZeroDivisionError:
        logger.error('Cannot divide by Zero')
        return None
    
# add(10, 10)
# substract(15, 10)
# multiply(5, 5)
# divide(100, 10)

# Lets try and divide by zero to get an error log
divide(10, 0)
