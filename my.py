def knapsack(k,a):
    a=sorted([(i,*j) for i,j in enumerate(a)],key=lambda x:-x[2]/x[1])
    n=len(a)
    r=[0]*n
    for i in range(n):
        while k>=a[i][1]:
            k-=a[i][1]
            r[a[i][0]]+=1
    return r

print(knapsack(100,((11.2,  7.4),
                                  (25.6, 17.8),
                                  (51.0, 41.2),
                                  (23.9, 15.6),
                                  (27.8, 19.0))))