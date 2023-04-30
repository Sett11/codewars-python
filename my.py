a='abcdefghijklmnopqrstuvwxyz'

def encode(s,k,n):
    c=list(filter(lambda e:e not in k,list(a)))
    b,r,i=[],[],0
    while i<len(k):
        if(k[i] not in b):
            b.append(k[i])
        i+=1
    c=b+c
    i=0
    while i<len(s):
        if(s[i] not in c):
            r.append(s[i])
        else:
            t=c.index(s[i])
            r.append(c[(t+n)%len(c)])
            n=t+1
        i+=1
    return ''.join(r)
    
def decode(s,k,n): 
    c=list(filter(lambda e:e not in k,list(a)))
    b,r,i=[],[],0
    while i<len(k):
        if(k[i] not in b):
            b.append(k[i])
        i+=1
    c=b+c
    i=0
    while i<len(s):
        if(s[i] not in c):
            r.append(s[i])
        else:
            t=c.index(s[i])
            v=t-n
            if(v<0):
                v+=len(c)
            r.append(c[v])
            n=v+1
        i+=1
    return ''.join(r)

print(encode("on","cryptogram",10))
print(decode("abc","keykeykeykey",10))
print(decode("jx","cryptogram",10))