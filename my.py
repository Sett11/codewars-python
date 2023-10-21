from re import sub,IGNORECASE


def jeringonza(s):
    return sub(r'[aioue]',lambda e:e.group()+('p' if e.group().islower() else 'P')+e.group(),s,flags=IGNORECASE)

print(jeringonza('jEringonzA'))