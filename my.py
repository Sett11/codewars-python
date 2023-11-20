from math import gcd
from re import sub

def binary_gcd(x,y):
    return len(sub(r'[^1]','',bin(gcd(x,y))))

print(binary_gcd(21,14))