def pentagonal(n):
   n-=1
   return (5*n**2+5*n+2)//2 if n>=0 else -1

print(pentagonal(77686))