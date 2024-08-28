from itertools import permutations

def rearranger(k,*args):
    d,M={},float('inf')
    for i in permutations(args):
        n=int(''.join(map(str,i)))
        if n%k==0:
            if n not in d:
                d[n]=[i]
            else:
                if i not in d[n]:
                    d[n].append(i)
            M=min(M,n)
    return f"Rearrangement: {' and '.join(', '.join([str(j) for j in i]) for i in d[M])} generates: {M} divisible by {k}" if d else 'There is no possible rearrangement'

print(rearranger(6, 19, 32, 2, 124, 20, 22))