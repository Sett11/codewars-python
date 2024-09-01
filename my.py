def start(f):
    a=[1,2]
    return f(a)

def end(a):
    return a.pop()

def push(a):
    return lambda x:lambda y:y([*a,x])
    
def add(a):
    s=a.pop()+a.pop()
    return lambda f:f([*a,s])

def sub(a):
    s=a.pop()-a.pop()
    return lambda f:f([*a,s])

def mul(a):
    s=a.pop()*a.pop()
    return lambda f:f([*a,s])

def div(a):
    s=a.pop()//a.pop()
    return lambda f:f([*a,s])

print((start)(push)(4)(push)(9)(div)(end))