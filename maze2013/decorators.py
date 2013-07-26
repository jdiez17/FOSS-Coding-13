from flask import jsonify, request
from functools import wraps

def json_output(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        return jsonify(result)

    return wrapper
