from flask import request, Response


def check_auth(username, password):
    """
    Checks whether a username/password combination is valid.
    """
    return username == 'hello' and password == 'Hell0'


def authentication_challenge():
    """
    Sends a 401 response that enables basic auth
    """
    message = 'Please, login with valid credentials to access this service.'
    headers = {
        'WWW-Authenticate': 'Basic realm="Login Required"'
    }
    return Response(message, 401, headers)


def authenticate_request():
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
        message = 'Please, login with valid credentials to access this service.'
        headers = {
            'WWW-Authenticate': 'Basic realm="Login Required"'
        }
        return Response(message, 401, headers)
    return None
