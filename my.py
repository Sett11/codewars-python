def isogram_encode(*a):
    if(len(a)!=2):
         return 'Incorrect key or input!'
    n,k=a
    if(len(set(k))!=10 or len(set(k))!=len(k) or not n):
            return 'Incorrect key or input!'
    try:
        n=list(map(int,str(n)))
        o={}
        for i in range(len(k)-1):
            o[i+1]=k[i]
        o[0]=k[-1]
        s=''
        for i in n:
            s+=o[i]
        return (s).upper()
    except:
        return 'Incorrect key or input!'

def isogram_decode(*a):
    if(len(a)!=2):
         return 'Incorrect key or input!'
    n,k=a
    if(len(set(k))!=10 or len(set(k))!=len(k) or not n):
            return 'Incorrect key or input!'
    try:
        n=list(n)
        o={}
        for i in range(len(k)-1):
            o[k[i]]=i+1
        o[k[-1]]=0
        return ''.join([str(o[i]) for i in n])
    except:
        return 'Incorrect key or input!'

    

print(isogram_encode(500, 'PATHFINDER'))
print(isogram_decode('FRR', 'PATHFINDER'))
print(isogram_decode())
print(isogram_encode())