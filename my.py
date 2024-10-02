from string import ascii_uppercase
from functools import reduce
from re import match

def f(n):
    r=''
    while n>=0:
        r=ascii_uppercase[n%26]+r
        n=n//26-1
    return r

def ff(s):
    return reduce(lambda a,c:a*26+ascii_uppercase.index(c)+1,s,0)

def spreadsheet(s):
    if match(r'^R\d+C\d+$',s):
        g=s.index('C')
        return str(f(int(s[g:][1:])-1))+s[:g][1:]
    g=next(i for i,j in enumerate(s) if j.isdigit())
    return f'R{s[g:]}C{ff(s[:g])}'