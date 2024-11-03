from collections import defaultdict

def closest_points_3d(a):
    d,n,m=defaultdict(list),len(a),1e9
    for i in range(n):
        for j in range(i+1,n):
            x,y=a[i],a[j]
            s=round((abs(y[0]-x[0])**2+abs(y[1]-x[1])**2+abs(y[2]-x[2])**2)**.5,5)
            m=min(m,s)
            d[s].append(sorted([x,y]))
    return [n,sorted(d[m]),m]

print(closest_points_3d([(33, 39, 34), (38, 9, 5), (19, 5, 16), (14, 4, 2), (34, 18, 35),\
         (26, 14, 1), (31, 38, 2), (37, 23, 8), (22, 38, 39), (20, 10, 10), (30, 23, 0),\
         (3, 34, 14), (11, 10, 33), (3, 5, 14), (36, 0, 10), (32, 15, 33), (26, 28, 12),\
         (11, 36, 6), (22, 9, 28), (30, 37, 27), (18, 20, 13), (32, 3, 13), (1, 23, 20),\
         (18, 32, 9), (31, 27, 29), (37, 19, 36), (0, 7, 16), (36, 17, 30), (9, 16, 19),\
         (15, 20, 29), (34, 29, 0), (21, 34, 36), (28, 23, 13), (0, 2, 39), (2, 12, 18),\
         (17, 31, 9), (15, 12, 24), (0, 0, 32), (31, 17, 29), (4, 26, 24)]))