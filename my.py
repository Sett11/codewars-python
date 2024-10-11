def validate_args(*args):
    def inner_func(func):
        def check(*w):
            for i in w:
                if not isinstance(i,args):
                    raise InvalidArgument()
            return func(*w)
        check.__name__=func.__name__
        check.__doc__=func.__doc__
        return check
    return inner_func


@validate_args(str)
def say_hello(name):
    """Say hello to {name}"""
    return "Hello, " + str(name)

@validate_args(int,float)
def f(a,b):
    return a+b

print(say_hello('Jhonny'))
print(f(1,2.0))
print(say_hello.__name__)