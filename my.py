class SnakesLadders():

    def __init__(self):
        self.a=[0,36,0,0,0,0,7,23,0,0,
                0,0,0,0,11,-10,0,0,0,0,
               21,0,0,0,0,0,0,56,0,0,
               0,0,0,0,0,8,0,0,0,0,
               0,0,0,0,0,-21,0,0,-38,0,
               16,0,0,0,0,0,0,0,0,0,
               0,-43,0,-4,0,0,0,0,0,0,
               20,0,0,-21,0,0,0,20,0,0,
               0,0,0,0,0,0,7,0,-21,0,
               0,-4,0,0,-20,0,0,0,-19,0]
        self.one=0
        self.two=0
        self.c=0
        self.v=1

    def play(self,d1,d2):
        if not self.v:
            return 'Game over!'
        s=d1+d2
        if not self.c:
            self.one+=s
            if self.one>100:
                self.one=100-(self.one-100)
            self.one+=self.a[self.one-1]
            if self.one==100:
                self.v=0
                return 'Player 1 Wins!'
            if d1!=d2:
                self.c=1
            return f'Player 1 is on square {self.one}'
        else:
            self.two+=s
            if self.two>100:
                self.two=100-(self.two-100)
            self.two+=self.a[self.two-1]
            if self.two==100:
                self.v=0
                return 'Player 2 Wins!'
            if d1!=d2:
                self.c=0
            return f'Player 2 is on square {self.two}'
        
r=SnakesLadders()
print(r.play(6,6))