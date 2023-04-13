import re
def calculate(e,v):
    e=re.sub(r'\&','and',e)
    e=re.sub(r'\|','or',e)
    for i in range(len(e)):
        if(e[i] in v):
            e=e.replace(e[i],str(v[e[i]]))
    return eval(e)

print(calculate("B & A | C", {"A": 1, "B": 0, "C": 1}))