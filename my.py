def f(a,q):
    n=len(a)
    z,v=q
    i=z-1
    j=z+1
    x=y=True
    while True:
        if not (x or y):
            break
        if i<0 or (v and a[i] in '[]'):
            x=False
        if j==n or (v and a[j] in '[]'):
            y=False
        if x:
            if not v and a[i] in '[]':
                for k in range(i-1,-1,-1):
                    if a[k] in '[]':
                        break
                i=k
            if a[i]=='C':
                a[i]='.'
                i-=1
            elif a[i]=='X':
                a[z]='.'
                x=False
            else:
                i-=1
        if y:
            if not v and a[j] in '[]':
                for k in range(j+1,n):
                    if a[k] in '[]':
                        break
                j=k
            if a[j]=='C':
                a[j]='.'
                j+=1
            elif a[j]=='X':
                a[z]='.'
                y=False
            else:
                j+=1
    return a

def hungry_foxes(s):
    a=list(s)
    c,r=False,[]
    for i,j in enumerate(a):
        if j in '[]':
            c=not c
        elif j=='F':
            r.append((i,c))
    [f(a,i) for i in r]
    return ''.join(a)

print(hungry_foxes("CCC[CCC]FCC[CCCCC]CFFFF[CCC]FFFF"))
print(hungry_foxes("CCC[CCC]FCC[CCCCC]CFFFF[CCC]FFFF"))