import datetime
from functools import wraps


def log_info(file_name):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            with open(file_name, 'a') as f:
                f.write("Function: {} was called at {}".format(func.__name__, datetime.datetime.now()))
            return func(*args, **kwargs)
        return decorator
    return accepter
