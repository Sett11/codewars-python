def proper_fractions(n):
    k=n>1 and n
    for i in range(2,int(n**.5)+1):
        if not n%i:
            k-=k//i
            while not n%i:
                n//=i
    if n>1:
        k-=k//n
    return k

print(proper_fractions(25))