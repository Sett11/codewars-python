def closest_points(a):
    n,m,d=len(a),1e6,{}
    for i in range(n):
        for j in range(n):
            if i!=j:
                c=round(((a[j][0]-a[i][0])**2+(a[i][1]-a[j][1])**2)**.5,4)
                m=min(m,c)
                if c not in d:
                    d[c]=[sorted([a[i],a[j]])]
                else:
                    x=sorted([a[i],a[j]])
                    if x not in d[c]:
                        d[c].append(x)
    return [n,sorted(d[m]),m]

print(closest_points([(8, 14), (16, 5), (5, 5), (15, 18), (17, 10), (0, 14), (4, 15),(19, 17), (13, 16), (10, 18), (14, 13), (12, 14), (11, 15), (7, 15)]))