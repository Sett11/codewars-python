import re

def Dragon(n,s='Fa'):
    return '' if type(n)!=int or n<0 else re.sub('a|b','',s) if n==0 else Dragon(n-1,re.sub(r'a|b',lambda e:'aRbFR' if e.group()=='a' else 'LFaLb',s))

print(Dragon(2))