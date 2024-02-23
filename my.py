def last_man_standing(n):
    a=list(range(1,n+1))
    while len(a)>1:
        del a[::2]
        a=a[::-1]
    return a[0]

print(last_man_standing(1000))