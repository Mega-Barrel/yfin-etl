"""Yfin time function logger"""

import time
from yfin.common.yfin_logger import logger

def time_it(func):
    """
    Get total time a module ran
    """

    def wrapper(*args, **kwargs):
        """"
        Wrapper class
        """
        start_time = time.time()
        func_name = func.__name__
        result = func(*args, **kwargs)
        end_time = time.time()
        message = f'Function {func_name} took {round(end_time - start_time, 2)} seconds to run'
        logger.info(message)
        return result
    return wrapper
