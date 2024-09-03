def max_ball(n):
   m=t=0
   c=1
   while c>=m:
      t+=1
      c=n*t/(3.6*10)-(.5*9.81*(t/10)**2)
      if c>m:
         m=c
      else:
         return t-1

print(max_ball(25))