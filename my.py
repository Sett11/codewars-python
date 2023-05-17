from functools import reduce as r

def count_of_heads(j,n,s):
    t=[]
    x=0
    while len(t)<s:
        x+=1
        t.append(x)
        j=j-1+r(lambda a,c:a*c,t)*n
    return j

print(count_of_heads(51,6,31))