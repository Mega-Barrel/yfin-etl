# Yfin Time Function Logger

The Yfin Time Function Logger is a Python decorator that can be applied to functions to log the total time taken for their execution. It uses the `time` module to measure the elapsed time and the `yfin.common.yfin_logger` module for logging the time information.

## Prerequisites

Before using the Yfin Time Function Logger, ensure that you have the following dependencies installed:

- time: This module is included in Python's standard library.
- yfin.common.yfin_logger: This module should be available in your project's directory.

## Usage

To use the Yfin Time Function Logger, follow these steps:

1. Import the necessary modules:

```python
import time
from yfin.common.yfin_logger import logger
```

Apply the time_it decorator to the functions you want to measure the execution time for:

```python
@time_it
def my_function(arg1, arg2):
    # Function code here
    pass
```

Call the decorated function as usual:
```python
my_function(arg1, arg2)
```

The decorator will log the total time taken for the function's execution.

## Functionality
- The time_it decorator wraps the decorated function in a wrapper function. 
- When the decorated function is called, the wrapper function measures the start and end time, calculates the elapsed time, and logs the information using the logger.info function. 
- The elapsed time is logged in seconds with two decimal places.

## Error Handling
- The Yfin Time Function Logger does not handle any exceptions. 
- It solely focuses on measuring and logging the execution time of the decorated functions. 
- If an exception occurs within the decorated function, it will propagate to the caller as usual.

## License
This project is licensed under the MIT License.