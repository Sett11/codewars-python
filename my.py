def f(e):
    if(e==''):return False
    else:return True

def is_defended(a,d):
    c=sum(a)
    b=sum(d)
    r=min(len(a),len(d))
    i=0
    while i<r:
        if(a[i]>d[i]):
            d[i]=''
        else:
            a[i]=''
        i+=1
    a=list(filter(f,a))
    d=list(filter(f,d))
    if(len(d)>len(a)):return True
    if(len(d)==len(a)):
        if(c>b):return False
        if(c<b or c==b):return True
    return False
    
print(is_defended([], [1,2,3]))