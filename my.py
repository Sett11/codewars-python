def strings_crossover(a,s):
   u,r=set(),0
   for i,j in enumerate(a):
      for k,c in enumerate(a):
         t=tuple(sorted([i,k]))
         if i!=k and t not in u:
            u.add(t)
            if all(y[0]==s[x] or y[1]==s[x] for x,y in enumerate(zip(j,c))):
               r+=1
   return r

print(strings_crossover(["abc", "aaa", "aba", "bab"],'bbb'))