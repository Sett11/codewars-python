def total(a):
    return a[0] if len(a)==1 else total([a[i]+a[i+1] for i in range(len(a)-1)])

print(total([1,2,3,4,5]))