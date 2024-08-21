power=lambda a:sum([[list(j) for j in __import__('itertools').combinations(a,i)] for i in range(len(a)+1)],[])

print(power([1,2,3]))