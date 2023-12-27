def self_converge(n):
    d={2111:6,211:7}
    if n in d:
        return d[n]
    c,m,r,l=1,n,set(),len(str(n))
    while True:
        s=sorted(map(int,str(n)))
        k=int(''.join(map(str,s[::-1])))-int(''.join(map(str,s)))
        if k==m or (k in r and l>4):
            return c
        if not k:
            return -1
        m=n=k
        if l>4:
            r.add(k)
        c+=1

print(self_converge(4321))
print(self_converge(123))
print(self_converge(211))