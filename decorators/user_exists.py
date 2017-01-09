from functools import wraps


def user_exists(func):
    @wraps(func)
    def decorator(self, user_id):
        if user_id is None:
            user_id = self.log_or_sign()
        else:
            user_id = self.change_user(user_id)
        return func(self, user_id)
    return decorator
