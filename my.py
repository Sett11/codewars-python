from collections import Counter
from functools import cache

@cache
def f(a,b):
    return '' if not (a and b) else a[0]+f(a[1:],b[1:]) if a[0]==b[0] else max(f(a[1:],b),f(a,b[1:]),key=len)

def is_merge(s,a,b):
    return f(s,a)==a and f(s,b)==b and Counter(s)==Counter(a+b)

print(is_merge('codewars', 'cdw', 'oears'))