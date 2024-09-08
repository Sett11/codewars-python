def shortest_arrang(n):
   for i in range(n//2+1,0,-1):
      t=[i]
      for j in range(n//2,0,-1):
         if j<t[-1]:
            t+=[j]
            if sum(t)==n:
               return t
         if sum(t)>n:
            break
   return [-1]

print(shortest_arrang(65))