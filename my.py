def wraps(func):
    def f(*args,**kwargs):
       return func
    f.__name__=func.__name__
    f.__doc__=func.__doc__
    return f