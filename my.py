def center(a):
    u=set(sum(a,()))
    for i in u:
        if all(i in j for j in a):
            return i
    return -1
    
print(center([(1,5),(4,5),(5,2),(3,5)]))