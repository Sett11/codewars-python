class UnexpectedTypeException(TypeError):
    ...

def expected_type(types):
    def inner_func(f):
        def func(*args,**kwargs):
            v=f(*args,**kwargs)
            if [i for i in types if isinstance(v,i)]:
                return v
            raise UnexpectedTypeException(f"Was expecting instance of: {', '.join(map(str,types))}")
        return func
    return inner_func

@expected_type((str,))
def return_something(input):
    return input

print(return_something(1))