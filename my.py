def geometric_sequence_sum(a,r,n):
    c,k=0,a
    for _ in range(n-1):
        c+=k*r
        k*=r
    return c+a

print(geometric_sequence_sum(2,2,10))