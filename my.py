import math

def thin_or_fat(l):
    for i in l:
        for j in i:
            if(j<0):
                return None
    i=0
    r=[]
    while i<len(l[0]):
        a=[]
        j=0
        while j<len(l):
            a.append(l[j][i])
            j+=1
        i+=1
        r.append(math.sqrt(sum(a)))
    c=sum([math.sqrt(sum(i)) for i in l])
    r=sum(r)
    if(r==c):
        return 'perfect'
    return 'fat' if r<c else 'thin'

print(thin_or_fat([[1,4,7], [2,5,8], [3,6,9]]))
print(thin_or_fat([[1,3], [5,7]]))
print(thin_or_fat([[-1,1,1], [-1,1,1], [1,1,1]]))