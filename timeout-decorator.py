import time
import signal
from functools import wraps

from typing import *

class TimoutException(Exception):
    pass

def timeout(seconds: int):
    def decorator(func: function):
        @wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimoutException(f'Function timed out after {seconds}')

            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)

            try:
                result = func(*args,**kwargs)
            finally:
                signal.alarm(0)
            return result
        return wrapper
    return decorator