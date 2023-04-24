def f(x,y):
    i=len(x)-1
    c=0
    t=0
    while i>=0:
        q=int(x[i])+int(y[i])
        if(q+t>9):
            t=1
        if(q+t<10):
            t=0
        if(q+t>9):
            c+=1
            t=1
        i-=1
    return c

def number_of_carries(a,b):
    a=str(a)
    b=str(b)
    if(len(a)<len(b)):
        a='0'*(len(b)-len(a))+a
    if(len(b)<len(a)):
        b='0'*(len(a)-len(b))+b
    return f(a,b)

print(number_of_carries(9999,1))