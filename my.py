from collections import Counter

def directions(g):
    c=Counter(g)
    r=[]

    for i,j in ['NS','SN','WE','EW']:
        r+=[i]*(c.get(i,0)-c.get(j,0))

    return r

print(directions(["S","S","N","E","W","S","N"]))
print(directions(["N","N","N","N","N","E","N","N"]))
print(directions(["N","W","S","E"]))