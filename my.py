def cyclic_string(s):
   n=len(s)
   r=n
   for i in range(n):
      for j in range(i+1,n+1):
         k=s[i:j]
         m=len(k)
         x=n//m+1
         if s in k*x:
            r=min(m,r)
   return r

print(cyclic_string('cabca'))