def stern_brocot(n):
    a=[1,1];c=1
    while n not in a:
            a.extend([a[len(a)-c]+a[len(a)-c-1],a[len(a)-c]])
            c+=1
    return a.index(n)

print(stern_brocot(19))