from functools import reduce as r
def maximum_product(a):
    i,q=0,[]
    while i<len(a):
        t=a.pop(i)
        q.append([r(lambda w,c:w*c,a,1),t])
        a.insert(i,t)
        i+=1
    return sorted(q,key=lambda e:(e[0],-e[1]),reverse=True)[0][1]

print(maximum_product([-1, 2, -3]))