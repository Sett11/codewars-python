from itertools import groupby as g

def kooka_counter(s):
    return len([list(j) for _,j in g([s[i:i+2] for i in range(0,len(s),2)])])

print(kooka_counter("HaHaHahahaHaHa"))