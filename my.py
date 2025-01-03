from math import log

def how_many_measurements(n):
    return 0 if n==1 else 1 if n<5 else int(log(n*3)/log(3))

print(how_many_measurements(8))