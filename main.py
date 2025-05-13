from collections import defaultdict

def bunch(n):
    s=bin(n)[2:]
    x,y,z,m,d=len(s),s.count('1'),0,1e3,defaultdict(list)
    while 1:
        t='0'*z+'1'*y+'0'*(x-y)
        z+=1
        x-=1
        w=sum(1 for j,k in zip(s,t) if j!=k)
        m=min(w,m)
        d[w].append(int(t,2))
        if t[-1]=='1':
            break
    return min(d[m])

print(bunch(52))
print(bunch(19))