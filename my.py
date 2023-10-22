def amaro_plan(n):
    r=[1 if i&1 else 0 for i,j in enumerate([0]*(n-1))]
    return [n*20-sum(r)]+r


print(amaro_plan(22))