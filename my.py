def next_id(a):
    if(not len(a)):
        return 0
    for i in range(max(a)+1):
        if(i not in a):
            return i
    return i+1

print(next_id([5,4,3,2,1,0]))