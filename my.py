def f(x):
    i=0
    a=[]
    while i<len(x[0]):
        j=0
        t=[]
        while j<len(x):
            if(i<len(x[j])):
                t.append(x[j][i])
            j+=1
        a.append(t)
        i+=1
    return a

def columnize(l,n):
    print(l,n)
    if(n==1):
        m=max(len(i) for i in l)
        return '\n'.join([i+(' '*(m-len(i))) for i in l])
    if(n>=len(l)):
        return ' | '.join(l)
    a=[]
    i=0
    while i<len(l):
        a.append(l[i:i+n])
        i+=n
    r=f(a)
    i=0
    while i<len(r):
        t=max([len(k) for k in r[i]])
        j=0
        while j<len(r[i]):
            if(len(r[i][j])<t):
                r[i][j]+=' '*(t-len(r[i][j]))
            j+=1
        i+=1
    return '\n'.join([' | '.join(i) for i in f(r)])