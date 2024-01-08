from collections import Counter
from math import gcd

def has_subpattern(s):
    a=sorted(i[1] for i in Counter(s).items())
    n,m=len(a),1e9
    for i in range(n):
        for j in range(i,n):
            m=min(m,gcd(a[i],a[j]))
    return all(i%m==0 for i in a) and m!=1

print(has_subpattern('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'))
print(has_subpattern('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'))