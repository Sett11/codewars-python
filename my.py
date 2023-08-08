from itertools import permutations as p
def solve(a):
    return len([q for q in [[int(h) for h in k.split('&')] for k in set(['&'.join([str(j) for j in sorted(i)]) for i in p(a,3)])] if q[1]-q[0]==q[2]-q[1]])

print(solve([0,1,2,3,5,6,7,11,13,15,17,19]))