from collections import Counter

def common(a,b,c):
    a,b,c=Counter(a),Counter(b),Counter(c)
    return sum(i*min(a[i],b[i],c[i]) for i in set(a)&set(b)&set(c))

print(common([1,2,2,3],[5,3,2,2],[7,3,2,2]))