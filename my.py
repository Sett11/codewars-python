from re import sub
from math import prod

def digit_multiplication(s):
    return eval(sub(r'\d+',lambda x:str(prod(map(int,x.group()))),s))

print(digit_multiplication("266-66"))
print(digit_multiplication("555"))