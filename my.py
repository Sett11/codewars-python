def find_spaceship(s):
    a=[e for e in [[[i,k] for k,h in enumerate(j) if h=='X'] for i,j in enumerate(s.split('\n')[::-1])] if e]
    return "Spaceship lost forever." if not a else a[0][0][::-1]

print(find_spaceship("..........\n..........\n.......X..\n..........\n.........."))
print(find_spaceship(""))