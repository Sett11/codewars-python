def goto(l,b):
    if(not isinstance(l,int) or not isinstance(b,str) or l<0 or l>3 or int(b)<0 or int(b)>3 or l==int(b)):return 0
    return -(l-int(b)) if(l>int(b)) else int(b)-l

print(goto(0,'2'))