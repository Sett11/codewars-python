from functools import reduce
from operator import mul
from re import sub


def find_middle(s):
    s=sub(r'\D','',s) if type(s)==str else ''
    if not s:
        return -1
    r=str(reduce(mul,map(int,s),1))
    l=len(r)//2-1
    return int(r[l+(1 if len(r)&1 else 0):l+2])


print(find_middle('58jd9fgh/fgh6s.,sdf'))
print(find_middle('asd.fasd.gasdfgsdfgh-sdfghsdfg/asdfga=sdfg'))