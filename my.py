def maxlen(a,b):
    c,d=max(a,b),min(a,b)
    return c/3 if c>=d*3 else c/2 if d>=c/2 else d

print(maxlen(5,17))