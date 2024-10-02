from string import ascii_uppercase
from functools import reduce

def f(n):
    r=''
    while n>=0:
        r=ascii_uppercase[n%26]+r
        n=n//26-1
    return r

def ff(s):
    return reduce(lambda a,c:a*26+ascii_uppercase.index(c)+1,s,0)
    

class SpreadSheetHelper:
    @staticmethod
    def convert_to_display(x):
        return str(f(int(x[0])))+str(x[1]+1)
    
    @staticmethod
    def convert_to_internal(x):
        g=next(i for i,j in enumerate(x) if j.isdigit())
        a,b=x[:g],x[g:]
        return ff(a)-1,int(b)-1

print(SpreadSheetHelper.convert_to_display((730,999)))
print(SpreadSheetHelper.convert_to_internal('ABC1000'))