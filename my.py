def howmuch(m,n):
   r=[]
   for i in range(min(m,n),max(m,n)+1):
      x,y=(i-1)/9,(i-2)/7
      if x%1==0 and y%1==0:
         r.append([f'M: {i}',f'B: {int(y)}',f'C: {int(x)}'])
   return r

print(howmuch(10000, 9950))