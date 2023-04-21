import re
def quicksum(s):
    if(len(re.sub(r'[A-Z ]','',s))):
        return 0
    a=[]
    for i,j in list(enumerate(list(map(lambda e:ord(e)-64 if e!=' ' else 0,s)))):
        a.append((i+1)*j)
    return sum(a)

print(quicksum("MID CENTRAL"))