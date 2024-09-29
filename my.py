from math import floor

class Chiken:
    def __init__(self,n):
        self.year=n
        self.egg=300
        self.death=False

    def action(self):
        if not self.death:
            t=self.egg
            self.year-=1
            self.egg=floor(self.egg-self.egg/100*20)
            if self.year==0:
                self.death=True
            return t
        return 0


def egged(n,k):
    if not n:
        return 'No chickens yet!'
    r,t=[],0
    for _ in range(n):
        r+=[Chiken(k) for _ in range(3)]
        t=sum(i.action() for i in r)
    return t

print(egged(74,10))