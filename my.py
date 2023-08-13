def best_parking_spot(a):
    r,m=[],float('inf')
    for i in [i for i,j in enumerate(a) if j=='OPEN']:
        for j in [i for i,j in enumerate(a) if j=='CORRAL']:
            t=abs(i-j)
            m=min(t+i,m)
            r.append([i,t,i+t])
    return sorted([i for i in r if i[2]==m],key=lambda e:(-e[0],e[1],e[2]))[0][0]

print(best_parking_spot(["STORE", "TAKEN", "TAKEN", "CORRAL", "TAKEN", "OPEN", "OPEN", "TAKEN", "CORRAL"]))
print(best_parking_spot(["STORE","OPEN","TAKEN","OPEN","CORRAL"]))