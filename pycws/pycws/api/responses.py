def OK(*data, message='OK.'):
    return {
        'status': 200,
        'message': message,
        'data': data
    }

def BAD_REQUEST(*data, message='Bad request.'):
    return {
        'status': 400,
        'message': message,
        'data': data
    }

def UNAUTHORISED():
    return {
        'status': 401,
        'message': 'You are not authorised to edit/create this object.',
        'data': []
    }

def NOT_FOUND(model, **kwargs):
    name = model.__name__.lower()
    params = ', '.join(f'{key}={value!r}' for key, value in kwargs.items())
    return {
        'status': 404,
        'message': f'No {name} with parameters {params} exists.',
        'data': []
    }

def METHOD_NOT_ALLOWED(method, path):
    return {
        'status': 405,
        'message': f'Method {method!r} is not allowed on {path!r}.',
        'data': []
    }

def BAD_API():
    return {
        'status': 500,
        'message': 'Misconfigured API. Please report this to the CWS staff.',
        'data': []
    }
