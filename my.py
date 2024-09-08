def factors(n):
   r=[[],[]]
   for i in range(2,int(n**.5)+1):
      if n%(i**2)==0:
         r[0].append(i)
      if n%(i**3)==0:
         r[1].append(i)
   return r

print(factors(81))