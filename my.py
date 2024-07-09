def f(n):
    return 1 if not n else n-m(f(n-1))

def m(n):
    return 0 if not n else n-f(m(n-1))

print(f(25),m(15))