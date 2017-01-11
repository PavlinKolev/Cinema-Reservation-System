from functools import wraps


def atomic(func):
    @wraps(func)
    def decorator(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
            self.cinema.commit_to_database()
            return result
        except:
            self.cinema.roll_back()
    return decorator
