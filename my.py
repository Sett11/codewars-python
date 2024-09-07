from itertools import combinations_with_replacement as c

def find(a,n):
   return len(sum([[list(j) for j in c(a,i) if sum(j)==n] for i in range(1,len(a)+1)],[]))

print(find([3,6,9,12],12))