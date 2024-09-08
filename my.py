from itertools import product
from functools import cache

@cache
def coin(n):
   return [''.join(i) for i in product('HT',repeat=n)]

print(coin(14))
print(coin(14))