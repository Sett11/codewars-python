def bs(a):
    l,r=0,len(a)
    while r-l>1:
        m=(l+r)//2
        if a[m]<m:
            l=m
        else:
            r=m
    return l+1

def index_equals_value(a):
    r=bs(a)
    return 0 if a[0]==0 else r if r<len(a) and a[r]==r else -1

print(index_equals_value((-3,0,1,3,10)))
print(index_equals_value(((-5, 1, 2, 3, 4, 5, 7, 10, 15))))
print(index_equals_value((0,)))