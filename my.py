import math
def median(l):
    return sum(sorted(l)[math.floor(len(l)/2)-1:math.floor(len(l)/2)+1])/2 if not len(l)&1 else sorted(l)[math.floor(len(l)/2)]

print(median([33,99,100,30,29,50]))
print(median([27, 974, 40, 706, 878]))