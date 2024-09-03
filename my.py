def nb_months(old,new,n,p):
   if new<=old:
      return [0,old-new]
   t,m=0,1
   while t<new:
      if m and m%2==0:
         p+=.5
      old-=old*p/100
      new-=new*p/100
      t=old+n*m
      m+=1
   return [m-1,round(t-new)]

print(nb_months(2000, 8000, 1000, 1.5))