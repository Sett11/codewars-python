import math
def factors(x,i=1):
    a=[]
    if(type(x)!=int or x<1):return -1
    while i<math.sqrt(x)+1:
        if(x%i==0):
            a.append(i);a.append(x/i)
        i+=1
    return sorted(list(map(int,list(set(a)))),reverse=True)

print(factors(54))