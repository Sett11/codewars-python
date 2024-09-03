def palin(a,b):
    n=int(str(1)+('0'*(a-1)))
    while b:
        s=str(n)
        if s==s[::-1]:
            b-=1
        n+=1
    return n-1

print(palin(6,20))