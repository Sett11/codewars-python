import math
def elevator(l,r,c):
    return 'right' if math.fabs(c-r)<=math.fabs(c-l) else 'left'

print(elevator(0,1,0))
print(elevator(0,1,1))
print(elevator(0,0,0))