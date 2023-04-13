def plastic_balance(a):
     if(len(a)==0 or sum([a[0],a[-1]])==sum(a[slice(1,-1)])):return a
     return plastic_balance(a[slice(1,-1)])

print(plastic_balance([1,2,3,4,5]))