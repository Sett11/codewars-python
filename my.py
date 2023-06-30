class HighScoreTable:
    def __init__(self,n):
        self.n=n
        self.scores=[]
    
    def update(self,n):
        self.scores.append(n)
        self.scores.sort(reverse=True)
        if len(self.scores)>=self.n:
            self.scores=self.scores[0:self.n]

    def reset(self):
       self.scores=[]

    
r=HighScoreTable(3)

r.update(10)
r.update(8)
r.update(12)
r.update(6)
r.update(10)
r.update(11)
print(r.scores)