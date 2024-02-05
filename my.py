class BullsAndCows:
    def __init__(self,n):
        self.s=list(str(n))
        self.v=True
        self.z=0
        if len(self.s)!=4 or n<0 or len(set(self.s))!=4:
                raise ValueError()
    
    def compare_with(self,n):
        if self.z>=8:
            return "Sorry, you're out of turns!"
        if self.v:
            if self.s==list(str(n)):
                    self.v=False
                    return "You win!"
            c,k,q=self.s.copy(),str(n),0
            if len(k)!=len(c) or n<0 or len(set(k))!=4:
                raise ValueError()
            for i in range(len(k)):
                if c[i]==k[i]:
                    q+=1
                    c[i]='&'
            l=len([i for i in k if i in c])
            self.z+=1
            return f"{q} bull{'s' if q!=1 else ''} and {l} cow{'s' if l!=1 else ''}"
        else:
            return "You already won!"


b=BullsAndCows(1234)
print(b.compare_with(12345))
print(b.compare_with(987))