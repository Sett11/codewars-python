from functools import reduce
def f(e):
    if(e==''):
        return False
    else:
        return True
    
def r(a,c):
    return int(a)+int(c)

def f_2(e):
    e=list(e)
    res=reduce(r,e)
    return res

def c(e):
    return int(e)

def largest_sum(s):
    if(s=='0'):return 0
    a=s.split('0')
    b=list(filter(f,a))
    x=list(map(f_2,b))
    return max(list(map(c,x)))

print(largest_sum("72102450111111090"))