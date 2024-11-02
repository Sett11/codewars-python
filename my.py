def knapsack(a,w):
    dp,m,r=[(0,[]) for _ in range(w+1)],0,{}
    for i in a:
        for j in range(w,0,-1):
            if i[0]<=j:
                x,y=dp[j-i[0]]
                if x+i[1]==dp[j][0]:
                    if m not in r:
                        r[m]=set()
                    r[m].add(tuple(sorted(y+[i[1]])))
                elif x+i[1]>=dp[j][0]:
                    dp[j]=(x+i[1],sorted(y+[i[1]]))
                m=max(m,dp[j][0])
    return [m,sorted([list(i) for i in set(map(tuple,[i[1] for i in dp if i[0]==m]+(list(tuple(list(map(list,r[m])) if m in r else []))))) if sum(i)==m])]

print(knapsack([(9, 4), (14, 12), (15, 6), (15, 6), (11, 12), (13, 6), (7, 13), (7, 7), (14, 20), (11, 16), (13, 12), (14, 11)],26))
print(knapsack([(11, 5), (19, 19), (4, 10), (18, 7), (16, 7), (18, 7), (7, 14), (17, 20)],40))
print(knapsack([(1, 19), (3, 20), (16, 14), (8, 4), (9, 6), (16, 17), (20, 4), (20, 15), (7, 9), (13, 13), (18, 2), (10, 10), (2, 1), (19, 7), (13, 19), (19, 1)],14))
print(knapsack([(2, 3), (6, 5), (8, 2), (4, 5), (2, 8), (5, 5), (2, 2)],7))