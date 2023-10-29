from operator import add

def running(lst, fn):
    r=[lst.pop(0)]
    for i in range(len(lst)):
        r.append(fn(r[-1],lst[i]))
    return r


print(running([1,1,1,1],add))
print(running([1,9,2,10],max))