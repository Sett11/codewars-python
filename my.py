from itertools import groupby

def check_sequence(s,l,n):
    return sum(1 for _,j in groupby(s) if len(list(j))==l)==n

print(check_sequence('HTHHHHHHHTTHHTHHTHTTHH',2,5))