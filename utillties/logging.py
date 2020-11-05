import inspect
import logging
import os
import stat


def getlogger():
    # log_dir = "/home/eli/Documents/Python_For_Selenuim/Python_e2e_108_Jenkins/tests"
    # os.chmod(log_dir, 0o777)

    loggername = inspect.stack()[1][3]
    logger = logging.getLogger(loggername)  # __import__()  --> for test case name
    logger.setLevel(logging.DEBUG)

    # create a file handler
    fileHandler = logging.FileHandler('logfile.log', mode='a+')  # create file to save all log file
    logger.addHandler(fileHandler)  # file handler object
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    return logger


# def getlogger():
#     logging.basicConfig(filename='logfile.log', format='%(asctime)s :%(levelname)s :%(name)s :%(message)s',
#                         level=logging.INFO)
#
#     logger = logging.getLogger()
#     return logger
