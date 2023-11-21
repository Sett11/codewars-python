a=[1]
q=[0,0,0]
d=[2,3,5]

def hamming(n):

    while len(a)<=n:
        p=[a[q[i]]*d[i] for i in range(3)]
        m=min(p)
        i=p.index(m)
        q[i]+=1
        if m!=a[-1]:
            a.append(m)

    return a[n-1]


print(hamming(4))
print(hamming(5))
print(hamming(1099))