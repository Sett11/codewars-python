def total_inc_dec(n):
   a,b,t=[1]*9,[1]*9,10
   for _ in range(2,n+1):
      c,d=[0]*9,[1]*9
      x=y=0
      for j in range(8,-1,-1):
         x+=a[j]
         c[j]+=x
         t+=c[j]
      for j in range(9):
         y+=b[j]
         d[j]+=y
         t+=d[j]
      t-=9
      a,b,c,d=c,d,a,b
   return t if n else 1

print(total_inc_dec(6))