from functools import wraps

def count_calls(func):
    @wraps(func)
    def counter(*args, **kwargs):
        counter.call_count += 1
        return func(*args, **kwargs)
    counter.call_count = 0
    return counter

def memoize(fn):
    cache={}
    def dec(n):
        if n in cache:
            return cache[n]
        r=fn(n)
        cache[n]=r
        return r
    dec.__name__=fn.__name__
    dec.__doc__=fn.__doc__
    return dec

@count_calls
@memoize
def fib(n):
    return [0,1][n] if n<=1 else fib(n-1)+fib(n-2)

print(fib(10))
print(fib.call_count)
print(fib(10))
print(fib.call_count)