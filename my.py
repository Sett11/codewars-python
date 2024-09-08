from itertools import groupby

def pop_blocks(a):
   b=[list(j) for _,j in groupby(a)]
   if all(len(i)==1 for i in b):
      return sum(b,[])
   b.pop(next(i for i,j in enumerate(b) if len(j)>1))
   return pop_blocks(sum(b,[]))

print(pop_blocks(['B', 'B', 'A', 'C', 'A', 'A', 'C']))
print(pop_blocks(['A', 'B', 'A', 'A', 'A', 'B', 'B']))