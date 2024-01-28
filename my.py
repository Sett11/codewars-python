def knapsack_light(a,b,c,d,m):
    return a+c if b+d<=m else max(a,c) if b<=m and d<=m else a if b<=m else c if d<=m else 0

print(knapsack_light(10,5,6,4,8))