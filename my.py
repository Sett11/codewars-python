from math import comb
from itertools import combinations
from functools import reduce
from operator import mul

def eval_prod_sum(a,nf,na,mv):
    if [i for i in a if isinstance(i,(str,float))] or [i for i in [nf,na,mv] if isinstance(i,(str,float)) or i<1]:
        return "Error. Unexpected entries"
    if nf>len(a):
        return "Error. Number of factors too high"
    if na>comb(len(a),nf):
        return "Error. Number of addens too high"
    smaller=equal=larger=0
    for i in combinations([reduce(mul,j) for j in combinations(a,nf)],na):
        t=sum(i)
        if t<mv:
            smaller+=1
        elif t>mv:
            larger+=1
        else:
            equal+=1
    return [{f"Below than {mv}": smaller}, {f"Equals to {mv}": equal}, {f"Higher than {mv}": larger}]

print(eval_prod_sum([-25, 42, -21, 14, -12, 26, -4],3,3,500))