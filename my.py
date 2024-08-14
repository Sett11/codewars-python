from math import ceil
from re import sub

def convert_recipe(s):
    def f(s):
        s=s.group()
        d,x={'tsp':5,'tbsp':15},s.split()
        return s+f" ({str(ceil(eval(x[0])*d[x[1]]))}g)"
    return sub(r'\d+\/*\d* (tsp|tbsp)',f,s)

print(convert_recipe("Add to the mixing bowl and coat well with 1 tbsp of olive oil & 1/2 tbsp of dried dill"))
print(convert_recipe("14/5 tsp of cinnamon" ))
