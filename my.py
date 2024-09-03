def bonus(a,s):
   m=min(a)
   r=[1/(i/m) for i in a]
   c=sum(r)
   return [round(s*i/c) for i in r]

print(bonus([18, 15, 12], 851))