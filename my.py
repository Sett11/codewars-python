from math import ceil

class Route:
    def __init__(self, s, n, m, t):
        self.s=s
        self.n=n
        self.m=m/60
        self.t=t
    
    def paperboys_needed(self):
        r=ceil(self.n/(self.t/self.m*50))-2
        return f'{r} paperboy{"" if r<2 else "s"} needed for {self.s}' if r>0 else "You and Stripes can handle the work yourselves"
    

R=Route("City Line", 466, 45, 1)

P=Route("Highland Park", 897, 35, .75)

print(R.paperboys_needed())

print(P.paperboys_needed())