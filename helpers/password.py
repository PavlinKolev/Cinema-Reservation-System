import hashlib


def encode(password):
    h = hashlib.sha512(password.encode())
    return h.hexdigest()
