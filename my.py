def swap_head_tail(a):
    o=a[len(a)//2+(0 if not len(a)&1 else 1):]
    return o+a[len(o):len(o)+(0 if not len(a)&1 else 1)]+a[:len(o)]

print(swap_head_tail([ 1, 2, -3, 4, 5, 6, -7, 8 ]))
print(swap_head_tail([1,2,3,4,5]))