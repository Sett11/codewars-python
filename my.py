from math import ceil

class Primes:
    @staticmethod
    def stream():
        n=15490000
        r=[True]*n
        r[0]=r[1]=False

        for i in range(2,int(n**.5+1)):
            if r[i]:
                r[i*2:n:i]=[False]*(ceil(n/i)-2)
        
        for i,j in enumerate(r):
            if j:
                yield i

print(next(Primes.stream()))