def missing(s):
    r=[]
    for i in range(1,7):
        n=int(s[:i])
        r.append(list(map(str,range(n,n+15))))
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

print(missing('998999100010011003'))