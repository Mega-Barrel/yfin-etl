"""Yfin time function logger"""

import time
from typing import Any

class CodeTime(object):
    """
    CodeTime class to log function execution time/seconds
    """

    def __init__(self, func):
        self.function = func

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        start = time.time()
        ret_fun = self.function(*args, **kwargs)
        fun_name = self.function.__name__
        end = time.time()

        print(f'Function {fun_name} took {round(end - start, 2)} seconds to run')
        return ret_fun
