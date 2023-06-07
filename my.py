def f(n):
    i,a=2,[]
    while i<=n*n:
        while(not (n%i)):
            n//=i
            a.append(i)
        i+=1
    s=set(a)
    return dict([(i,a.count(i)) for i in s])
class PrimeFactorizer:
    def __init__(self,n):
        self.n=n
        self.factor=f(self.n)
    

    
print(PrimeFactorizer(24).factor)