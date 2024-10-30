from collections import Counter

def count_contiguous_distinct(k,a):
    n,q=len(a),Counter(a[:k])
    r=[len(q)]
    for i in range(n-k):
        if a[i] in q:
            q[a[i]]-=1
            if not q[a[i]]:
                del q[a[i]]
        if a[i+k] not in q:
            q[a[i+k]]=0
        q[a[i+k]]+=1
        r.append(len(q))
    return r

print(count_contiguous_distinct(2,[1, 2, 1, 3, 4, 2, 3,3]))