j=[0, 0, 1, 2, 2, 3]
a=[1, 1, 2, 2, 3, 3]


def john(n):
    while len(j)<=n:
        k=len(j)
        j.append(k-a[j[k-1]])
        a.append(k-j[a[k-1]])
    return j[:n]

def ann(n):
    while len(a)<=n:
        k=len(a)
        a.append(k-j[a[k-1]])
        j.append(k-a[j[k-1]])
    return a[:n]
    
def sum_john(n):
    if len(j)<n:
        john(n+1)
    return sum(j[:n])
    
def sum_ann(n):
    if len(a)<n:
        ann(n+1)
    return sum(a[:n])

print(sum_john(75))
print(sum_ann(115))