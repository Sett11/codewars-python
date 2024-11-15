from time import sleep
from time import time


def timer(n):
    def inner_func(f):
        def func(*args,**kwargs):
            s=time()
            f(*args,**kwargs)
            return time()-s<=n
        return func
    return inner_func

@timer(1)
def foo():
    sleep(0.1)

print(foo())