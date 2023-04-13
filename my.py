import math
def crazy_formula(n):
    n=list(map(int,str(n)))
    if(len(n)%2)==0:
        n=n[slice(0,len(n)-1)]
    if(n[math.floor(len(n)/2)]%2!=0):
        n[math.floor(len(n)/2)]=-n[math.floor(len(n)/2)]
    if(n[math.floor(len(n)/2)]%2)==0 and (n[len(n)-1]%2)==0:
        n[len(n)-1]=-n[len(n)-1]
    if(n[math.floor(len(n)/2)]%2)==0 and (n[len(n)-1]%2)!=0:
        n[0]=n[0]**2
    n=abs(sum(n))
    return n if len(str(n))==1 else crazy_formula(n)

print(crazy_formula(214))
print(crazy_formula(2234))
print(crazy_formula(77633658797932970))