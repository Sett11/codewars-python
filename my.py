import math

def even_digit_squares(a,b):
    return [i**2 for i in range(math.floor(math.sqrt(a))+1,math.ceil(math.sqrt(b))+1) if all(map(lambda e: not int(e)&1,list(str(i**2))))]

print(even_digit_squares(10000,40000))