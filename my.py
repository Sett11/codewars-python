class LCG:
  a = 2
  c = 3
  m = 10
  
  def __init__(self,seed):
      self.seed = seed
  
  def random(self):
     n=((self.a*self.seed+self.c)%self.m)
     self.seed=n
     return n/10
  
r=LCG(5)

print(r.random())
print(r.random())
print(r.random())
print(r.random())