def optimal_number_of_coins(n,a):
    r=[0]+[n+1]*n
    for i in range(1,n+1):
        for j in a:
            if j<=i:
                r[i]=min(r[i],r[i-j]+1)
    return -1 if r[n]>n else r[n]


print(optimal_number_of_coins(33,[1, 6, 9, 10]))