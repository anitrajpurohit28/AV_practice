import logging
import inspect

"""
Steps to create your own custom logger
1. Creation of logger object and set log level
2. Creation of handler object and set log level
    Can create more than one handler object like StreamHandler, logging.FileHandler etc
3. Creation of formatter object
4. set formatter object to handler created in step 2
5. Add handler object to logger created in step 1
6. Log the message using logger object
"""
def get_my_logger(level=logging.DEBUG):
    # print(inspect.stack())
    # for i, x in enumerate(inspect.stack()[0]):
    #     print(i, " :: ", x)
    # print()
    # for i, x in enumerate(inspect.stack()[1]):
    #     print(i, " :: ", x)

    caller_name = inspect.stack()[1][3]
    # 1. Creation of logger object and set log level
    logger = logging.getLogger(caller_name)
    logger.setLevel(level)

    # 2. Creation of handler object and set log level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # 3. Creation of formatter object

    # Not printing date and logger details as it is a local program
    # formatter = logging.Formatter('%(asctime)s:%(name)s:%(levelname)s:%(message)s',
    #                               datefmt='%d-%m-%y %H:%M:%S')
    formatter = logging.Formatter('%(name)s:%(message)s')

    # 4. set formatter object to handler created in step 2
    console_handler.setFormatter(formatter)
    # 5. Add handler object to logger created in step 1
    logger.addHandler(console_handler)
    return logger


"""
# Ways of getting current function name
print(inspect.stack()[0][0].f_code.co_name)
print(inspect.stack()[0][3])
print(inspect.currentframe().f_code.co_name)
print(sys._getframe().f_code.co_name)

# Ways of getting caller function name
print(inspect.stack()[1][0].f_code.co_name)
print(inspect.stack()[1][3])
print(inspect.currentframe().f_code.co_name)
print(sys._getframe().f_code.co_name)
"""