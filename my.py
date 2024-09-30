def f(a,b):
    if b==0:  
        return a,1,0
    else:
        d,x,y=f(b,a%b)
        return d,y,x-y*(a//b)

class RSA:
    def __init__(self,p,q,e):
        self.e=e
        self.n=p*q
        self.d=f(self.e,(p-1)*(q-1))[1]
    
    def encrypt(self,m):
        return pow(m,self.e,self.n)
    
    def decrypt(self,c):
        return pow(c,self.d,self.n)

r=RSA(61,53,17)
print(r.encrypt(665))
print(r.decrypt(640))