import math
def reverse_middle(a):
    a=a[slice(len(a)//2-1,math.ceil(len(a)/2)+1)]
    a.reverse()
    return a

print(reverse_middle([1, 2, 4, 5]))