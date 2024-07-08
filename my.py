def add(a):
    def f(b):
        return a+b
    return f

def subtract(a):
    def f(b):
        return a-b
    return f
    
def multiply(a):
    def f(b):
        return a*b
    return f
    
def apply(f):
    return f

print(apply(add)(5)(7))