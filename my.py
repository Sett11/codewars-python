from itertools import product

def multiiter(*args):
    for k in [tuple(j) for j in product(*[list(range(i)) for i in args])]:
        yield k

print(list(multiiter(3,2)))