def func(n):
    return not n&1

def map(a,f):
    return 'given argument is not a function' if not isinstance(f,type(func)) else 'array should contain only numbers' if not all(type(i)==int or i.isdigit() for i in a) else [f(int(i)) for i in a]

print(map([1,2,3,4,5,6,7,'8',9,10],func))