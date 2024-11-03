from math import comb

def get_participants(n):
    return next(i for i in range(55) if comb(i,2)>=n)

print(get_participants(700))