from hashlib import md5
from itertools import product

a=[''.join(i) for i in product('0123456789',repeat=5)]

def crack(h):
    return next(i for i in a if md5(bytes(i,'utf-8')).hexdigest()==h)

print(crack('827ccb0eea8a706c4c34a16891f84e7b'))