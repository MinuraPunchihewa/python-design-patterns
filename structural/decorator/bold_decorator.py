
def bold(function):
    def wrapper(*args, **kwargs):
        return '<b>' + function(*args, **kwargs) + '</b>'
    return wrapper