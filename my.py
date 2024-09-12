from random import choice,randint
from functools import reduce

def choose_move(a):
    n=reduce(lambda x,y:x^y,a)
    r=[[i,j^n] for i,j in enumerate(a) if j^n<j]
    if not r:
        x,y=choice(list(enumerate(a)))
        return [x,randint(1,y)]
    x,y=min(r,key=lambda i:i[1])
    return [x,a[x]-y]

print(choose_move((0, 6, 3, 6, 6, 3, 7, 5, 3, 3)))
print(choose_move((0,3,5)))
print(choose_move((3,3,6)))