from math import gcd

def nbr_of_laps(x,y):
   if x==y:
      return 1,1
   n=gcd(x,y)
   if n==1:
      return (x,y)[::-1]
   t=max(x,y)/n,min(x,y)/n
   return t if y>x else tuple(sorted(t))
    
print(nbr_of_laps(2487, 3628))
print(nbr_of_laps(4,6))