def elimination(a):
    a=list(filter(lambda e:e!='',[i if a.count(i)>1 else '' for i in a]))
    return a[0] if len(a) else None

print(elimination([2, 5, 34, 1, 22]))