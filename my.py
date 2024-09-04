def coffee_limits(a,b,c):
   n=k=int(''.join(map(lambda x:str(x).rjust(2,'0'),[a,b,c])))
   x,y,r=int('CAFE',16),int('DECAF',16),[0]*2
   vn=vk=True
   for i in range(1,5001):
      if vn:
         n+=x
         if 'DEAD' in hex(n).upper():
            vn=False
            r[0]=i
      if vk:
         k+=y
         if 'DEAD' in hex(k).upper():
            vk=False
            r[1]=i
      if not vn and not vk:
         break
   return r

print(coffee_limits(1950, 1, 19))