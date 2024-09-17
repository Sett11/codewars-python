def fortune(f0,p,c0,n,i):
    p/=100
    i/=100
    for _ in range(n-1):
        f0+=(f0*p)-c0
        c0+=c0*i
    return f0>0.3 or f0==0.0

print(fortune(100000, 1, 2000, 15, 1))
print(fortune(100000, 1, 9185, 12, 1))