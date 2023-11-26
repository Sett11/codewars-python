def generate_sequence(n,m):
    a,r=list(range(n,m)),[]
    l=len(a)

    for i in range(l//2):
        r.append(a[i])
        r.append(a[l-i-1])
    
    return r+([a[l//2]] if l&1 else [])

print(generate_sequence(1,12))