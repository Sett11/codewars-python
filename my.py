def build_a_wall(x=None,y=None):
    try:
        if x*y>10000:
            return "Naah, too much...here's my resignation."
        return '\n'.join(([('■■ '*y)[:-1].replace(' ','|')]+['■|'+i+'|■' if not j&1 else i for j,i in enumerate([('■■ '*(y if i&1 else y-1))[:-1].replace(' ','|') for i in range(x-1)])])[::-1]) or None if x>0 and y>0 else None
    except:
        pass

print(build_a_wall(29,3))