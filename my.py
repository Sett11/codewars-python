from re import sub,search,findall
from collections import Counter

def parse_molecule(s):
    tok=lambda x:[''.join(i) for i in findall(r'([A-Z][a-z])|([A-Z])',x)]
    def f1(s):
        k=s.group()
        return ''.join(i for i in k if i.isalpha())*int(''.join(i for i in k if i.isdigit()))
    def f2(s):
        s=s.group()
        g=s.rfind(')')
        j=int(s[g+1:] or 1)
        return ''.join(i*j for i in tok(s[1:g]))
    s,r=sub(r'(([A-Z][a-z]|[A-Z])\d+)',f1,sub(r'\{|\[','(',sub(r'\}|\]',')',s))),r'\(([A-z]+)\)\d*'
    while search(r,s):
        s=sub(r,f2,s)
    return Counter(tok(s))

print(parse_molecule("(C5H5)Fe(CO)2CH3"))