from collections import Counter
from bisect import insort


def merge_arrays(a,b):
    s,x,y,r=set(a)|set(b),Counter(a),Counter(b),[]
    for i in s:
        if i in x:
            if i not in y or x[i]==y[i]:
                insort(r,i)
        else:
            if i not in x or x[i]==y[i]:
                insort(r,i)
    return r

print(merge_arrays([10,10,10, 15, 20, 20, 25, 25, 30, 7000],[10, 15, 20, 20, 27, 7200]))