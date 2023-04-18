def range_function(*a):
    b=[*a]
    if(len(b)==1):return list(range(1,b[0]+1))
    if(len(b)==2):return list(range(b[0],b[1]+1))
    if(len(b)==3):return list(range(b[0],b[2]+1,b[1]))

print(range_function(2,3,15))