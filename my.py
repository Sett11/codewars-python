def hypertensive(l):
    l=[list(map(lambda e:e.split('/'),i)) for i in l]
    i=0
    r=[]
    while i<len(l):
        j=0
        a=[]
        b=[]
        c=[False]
        while j<len(l[i]):
            a.append(int(l[i][j][0]))
            b.append(int(l[i][j][1]))
            if(int(l[i][j][0])>=180 and int(l[i][j][1])>=110):
                c[0]=True
            j+=1
        r.append([sum(a)/len(a),sum(b)/len(b),len(b),c[0]])
        i+=1
    return len(list(filter(lambda e:e[0]>=140 and e[2]>1 or e[1]>=90 and e[2]>1 or e[3],r)))


print(hypertensive([["130/90","140/94"],["160/110"],["200/120"],["150/94","140/90","120/90"],["140/94","140/90","120/80"]]))
print(hypertensive([['160/90', '118/74'], ['160/110'], ['200/90', '120/80', '116/76', '140/120', '110/64', '114/72'], ['150/92', '140/90', '120/80'], ['140/94', '140/90', '120/80']]
))