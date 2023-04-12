import math
def halving_sum(n):
    c=n
    while n!=1:
        n=math.floor(n/2)
        c+=n
    return c

print(halving_sum(127))