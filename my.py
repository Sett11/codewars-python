from functools import reduce
from operator import mul

def numbers_with_digit_inside(x,d):
    a=[i for i in range(1,x+1) if str(d) in str(i)]
    return [len(a),sum(a),reduce(mul,a,1) if a else 0]

print(numbers_with_digit_inside(11,1))
print(numbers_with_digit_inside(1,0))