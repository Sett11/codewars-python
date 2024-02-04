def powers(n):
    r,q,i=[],[],1
    while i<=n:
        r.append(i)
        i*=2
    for i in r[::-1]:
       while n>=i:
           q.append(i)
           n-=i
    return q[::-1]

print(powers(621588920))