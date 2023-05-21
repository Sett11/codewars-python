import random as r

def make_password(l,a,b,c):
    alf=list('abcdefghijklmnopqrstuvwxyz')
    u_alf=list(''.join(alf).upper())
    n=list('0123456789')
    arr=[i[0] for i in [[alf,b],[u_alf,a],[n,c]] if(i[1])]
    s=''
    i=0
    while len(s)<l:
        i%=len(arr)
        n=r.randrange(0,(len(arr[i])))
        s+=arr[i].pop(n)
        arr=[i for i in arr if len(i)]
        i+=1
    return s

print(make_password(5,True,True,True))