from math import comb

def routes(n):
    return comb(n*2,n) if n>0 else 0

print(routes(8))