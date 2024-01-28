def rounding(n,m):
    a,_=divmod(n,m)
    if m-n<n and m>n:
        return m
    return n if (m%n==0 or n%m==0) and n>1 else m*a+(m if m*a+m-n<abs(m*a-n) else 0) if a else 0

print(rounding(20,3))
print(rounding(19,3))
print(rounding(50,100))
print(rounding(154,4))
print(rounding(851,46))
print(rounding(497,536))