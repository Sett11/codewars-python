from collections import Counter

def histogram(a,b):
    if not a:
        return []
    a,r=sorted(Counter(a).items()),[]
    for i in range(0,a[-1][0]+1,b):
        r.append(sum([j[1] for j in a if i<=j[0]<i+b]))
    return r

print(histogram([1, 1, 0, 1, 3, 2, 6], 1))