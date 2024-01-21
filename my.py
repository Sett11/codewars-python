def fib_rabbits(n,k):
    a,b=k,1
    while n>2:
        c=a
        a=b*k
        b+=c
        n-=1
    return b if n else 0

print(fib_rabbits(8,12))