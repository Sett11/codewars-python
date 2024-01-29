def f(n):
    return [str(i) for i in range(n,n+15)]

def missing(s):
    r=[]
    for i in range(1,7):
        r.append(f(int(s[:i])))
    for a in r:
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