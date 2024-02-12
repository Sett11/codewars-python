from fractions import Fraction as f
from functools import reduce as r

add_fracs=lambda *args:str(r(lambda a,c:f(a)+f(c),args) if args else '')

print(add_fracs('2/3', '1/3', '4/6'))