def largest(n):
    check=lambda x:all(x%i for i in range(2,int(x**.5+1)))
    try:
        k=int('9'*n)
        while not check(k):
            k-=1
        return k
    except:
        return False

print(largest(5))