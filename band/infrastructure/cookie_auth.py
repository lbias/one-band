import hashlib

from datetime import timedelta

auth_cookie_name = 'band'


def set_auth(request, user_id):
    hash_val = __hash_text(user_id)
    val = "{}:{}".format(user_id, hash_val)

    request.add_response_callback(lambda req, resp: __add_cookie_callback(
        req, resp, auth_cookie_name, val
    ))


def __add_cookie_callback(_, response, name, value):
    response.set_cookie(name, value, max_age=timedelta(days=30))
