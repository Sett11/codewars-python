def func_or(a,b):
    r=[a,b]
    return all(i for i in r) or any(i for i in r)

def func_xor(a,b):
    r=[a,b]
    return not all(i for i in r) and any(i for i in r)