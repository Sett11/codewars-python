i=0

def random_ints(n,t):
    global i
    a=[t-i]+[0]*(n-i-1)+[i]
    i+=1
    if i>t:
        i=0
    while len(a)<n:
        a.append(1)
        a[0]-=1
    if len(a)>n:
        a.pop(a.index(0))
    return a

print(random_ints(5,296))
print(random_ints(9,39))
print(random_ints(9,39))
print(random_ints(8,307))