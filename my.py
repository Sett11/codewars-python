from itertools import permutations as p
def slogan_maker(a):
    return [' '.join(i) for i in p([ k[1] for k in sorted([[a.index(j),j] for j in set(a)])])]

print(slogan_maker(["super", "guacamole", "super", "super", "hot", "guacamole"]))