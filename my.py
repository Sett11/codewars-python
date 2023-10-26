from collections import Counter

r=[]

def res(v):
    for i,k in r:
        if i==v:
            return k
    return -1

def construct_square(s):
    v=sorted(Counter(s).values())
    i=0
    if r and len(str(r[0][1]))>=len(s):
        return res(v)
    while len(str(i**2))<=len(s):
        n=i**2
        r.insert(0,[sorted(Counter(str(n)).values()),n])
        i+=1
    return res(v)


print(construct_square('aaaabbcde'))