def full_cycle(a):
    n,u=len(a),set()
    i=j=0
    while j<=n:
        t=a[i]
        if t in u and len(u)==n:
            return True
        u.add(t)
        i=t
        j+=1
    return False

print(full_cycle([2, 0, 1]))