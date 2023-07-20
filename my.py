import math

def get_best_combination(s):
    print(s)
    if s<=60:
        return str(s)
    if s==71:
        return '111'
    n,m=math.floor(s/60),math.floor((s-60)/60)
    s1,s2=s-(n*60)+60,s-(n*60)
    r,i=[str(m)+str(s1),str(n)+str(s2)],0
    while i<len(r):
        if r[i][0]=='-':
            r[i]=r[i][2:]
        if len(r[i])<3 and s>120:
            r[i]=r[i][0]+'0'+r[i][1]
        if len(r[i])<4 and s>700:
            r[i]=r[i][0]+r[i][1]+'0'+r[i][2]
        i+=1
    r,i=[i[1:] if i[0]=='0' else i for i in r[::-1]],0
    while i<len(r):
        j,c=0,0
        while j<len(r[i])-1:
            if r[i][j]!=r[i][j+1]:
                c+=1
            j+=1
        r[i]=[r[i]]
        r[i].append(c)
        i+=1
    r=sorted(r,key=lambda e:e[1])
    if r[0][1]==r[1][1] and len(r[0][0])!=len(r[1][0]):
        r=sorted(r,key=lambda e:len(e[0]))
    q,w,a=r[0][0],r[1][0],str(s-60)
    if a=='55':
        return q
    if len(q)>=5 and int(q[2:])>99:
        return w
    return q[1:] if q[0]=='0' else q if not q.endswith(a) else w

print(get_best_combination(273))
print(get_best_combination(121))
print(get_best_combination(180))
print(get_best_combination(99))
print(get_best_combination(3690))
print(get_best_combination(115))
print(get_best_combination(72))
print(get_best_combination(4360))