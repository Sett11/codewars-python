from functools import reduce
def f(a,b):
    a+=b
    return a
def hello_world():
    return reduce(f,map(chr,[72, 101, 108, 108, 111, 44, 32, 87, 111, 114, 108, 100, 33]))

print(hello_world())