def comb(a,s,x=6):
    n,t,r=len(a),list(range(x)),[]
    def f():
        w=[a[i] for i in t]
        if ''.join(s[i] for i in w)=='banana':
            r.append(w+[n])
    while 1:
        f()
        for i in reversed(range(x)):
            if t[i]!=i+n-x:
                break
        else:
            return r
        t[i]+=1
        for j in range(i+1,x):
            t[j]=t[j-1]+1

def bananas(s):
    n=len(s)
    return list(map(lambda x:('-'*x[0] if x[0] else '')+''.join(s[x[i]]+'-'*(x[i+1]-x[i]-1) for i in range(len(x)-1)),comb(list(range(n)),s,6)))

print(*bananas('bbananana'),sep='\n')