def bouncy_count(n):
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
   return 10**n-t if n else 0

print(bouncy_count(4))