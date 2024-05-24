def all_nines(x):
    if x%2==0:
        return -1
    n='9'
    for _ in range(2500):
        t=int(n)//x
        if t*x==int(n):
            return t
        n+='9'
    return -1

print(all_nines(323))