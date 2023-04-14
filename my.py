def only_one(*a):
    b=[];c=[]
    for i in a:
        if(i):b.append(i)
        else:c.append(i)
    return len(b)==1 and len(c)>0 if len(a)>0 else False

print(only_one())