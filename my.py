from itertools import permutations as p

def late_clock(a,b,c,d):
    r=max(filter(lambda z:int(z[:2])<24 and int(z[2:])<60,map(lambda x:''.join(map(lambda y:str(y),x)),p([a,b,c,d]))))
    return f'{r[:2]}:{r[2:]}'


print(late_clock(9,1,2,5))