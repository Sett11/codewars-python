def nth_floyd(n):
    a=b=0
    while b<n:
        a+=1
        b+=a
    return a

print(nth_floyd(212))