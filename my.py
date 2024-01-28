def f(n):
    return [str(i) for i in range(n,n+15)]

def missing(s):
    r=[]
    for i in range(1,7):
        n=int(s[:i])
        r.append([n,f(n)])
    for _,a in r:
        q=[]
        for i in range(len(a)):
            q.append(a[i])
            if ''.join(q)==s:
                return -1
            t=a.copy()
            p=int(t.pop(i))
            t=''.join(t)[:len(s)]
            if t==s:
                return p
    return -1
            
print(missing('599600601602'))
print(missing('899091939495'))
print(missing('9899101102'))
print(missing('99991000110002'))