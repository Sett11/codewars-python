def is_smooth(a):
    return a[0]==sum(a[slice(len(a)//2-1,-len(a)//2+1)]) and a[0]==a[len(a)-1] if len(a)%2==0 else a[0]==a[len(a)//2] and a[0]==a[len(a)-1]

print(is_smooth([-12, 34, 40, -5, -12, 4, 0, 0, -12]))
print(is_smooth([7, 2, 2, 5, 10, 7]))