from re import split,findall
from functools import reduce

def f(e,x):
    k,p=split(r'x\^?',e)
    k,p=-1 if k=='-' else 1 if k=='' else int(k),1 if p=='' else int(p)
    return p*k*pow(x,p-1)

def differentiate(e,p):
    return reduce(lambda a,c:a+f(c,p),[i[0] for i in findall(r'(-?\d*x(\^\d+)?)',e)],0)

print(differentiate("-5x^2+10x+4", 3))