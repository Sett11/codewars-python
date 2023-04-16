from functools import reduce
def math_engine(a):
    if(a==None):return 0
    if(type(a)==list and len(a)==0):return 1
    b=list(filter(lambda e:e>=0,a));c=list(filter(lambda e:e<0,a))
    return (reduce(lambda a,c:a*c,b,1) if b else 1)+(reduce(lambda a,c:a+c,c,0) if c else 0) if a else 0

print(math_engine([0]))