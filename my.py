import re

records= (
    ('0001', '001', 12),
    ('0012', '001', 1000),
    ('0012', '001', 32),
    ('0027', '007', 207),
    ('0112', '007', 12119),
    ('1009', '007', 200)
)

def f(a):
    i=0
    while i<len(a):
        a[i],j=list(a[i]),i+1
        while j<len(a):
            if a[i][0]==a[j][0]:
                a[i][2]+=a[j][2]
                a[j]=[0,0,0]
            j+=1
        i+=1
    a,t=[i for i in a if i!=[0,0,0]],[f'Group: {a[0][1]}']
    r,i,s=[' '.join([f'    Product; {i[0]}',f'Value: {i[2]}']) for i in a],0,f'    Group total: {sum([i[2] for i in a])}'
    while len(s)<38:
        s=re.sub(r':',': ',s)
    while i<len(a):
        while len(r[i])<31:
            r[i]=re.sub(r':',': ',r[i])
        r[i]=re.sub(r';',':',r[i])
        i+=1
    return t+r+[s]

def generate_report(r):
    r=list(r)
    if len(r)==1:
        r.append((r[0][0],r[0][1],0))
    r,a,i,s=sorted(r,key=lambda e:(int(e[1]),int(e[0]),e[2])),[],1,f'Total: {sum([i[2] for i in r])}'
    while len(s)<38:
        s=re.sub(r':',': ',s)
    while i<len(r):
        if r[i][1]!=r[i-1][1]:
            a.append(r[:i])
            r,i=r[i:],0
        if r[i][1]==r[i-1][1] and i==len(r)-1:
            a.append(r[:i+1])
        i+=1
    return ('\n'.join(['\n'.join(f(i))+'\n' for i in a])+('\n' if r else '')+s).rstrip()

print(generate_report(records))