import re
def evenator(s):
    return ' '.join(list(map(lambda e: e+e[len(e)-1] if len(e)%2!=0 else e,re.sub(r'[.,?!_]','',s).split())))

print(evenator('underscore is not considered a word..in this case,'))