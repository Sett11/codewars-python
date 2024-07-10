# validate_number=lambda s:['Plenty more fish in the sea','In with a chance'][bool(__import__('re').match(r'^(0|\+44)7([\d-]){9,9}$',s.replace('-','')))]

# print(validate_number('87454876120'))
# print(validate_number('+447454876120'))

class Mem:
    def __init__(self):
        self.ndp=[3,7,11]
    
    def check(self,n):
        return all(n%i for i in range(2,int(n**.5)+1))

    def req(self,n):
        if len(self.ndp)>=n:
            return self.ndp[n-1]
        i=self.ndp[-1]+1
        while len(self.ndp)<=n:
            if i%4==3 and self.check(i):
                self.ndp.append(i)
            i+=1
        return self.ndp[n-1]

m=Mem()

def ith_nondecomp_prime(n):
    return m.req(n)

print(ith_nondecomp_prime(30))