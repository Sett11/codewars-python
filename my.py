import math as m

def f(x):
  if(x<2):
    return False
  if(x==2):
    return True
  i=2
  while i<m.sqrt(x)+1:
    if(x%i==0):
      return False
    i+=1
  return True
  

def summationOfPrimes(n):
  i=2
  a=[]
  while i<=n:
    if(f(i)):
      a.append(i)
    i+=1
  return sum(a)
  
print(summationOfPrimes(10))