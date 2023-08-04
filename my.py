import heapq as h

def add_all(l): 
    h.heapify(l)
    r=0
    while len(l)>1:
        a,b=h.heappop(l),h.heappop(l)
        r+=a+b
        h.heappush(l,a+b)
    return r

print(add_all([1,2,3,4]))