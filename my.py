def max_profit(a):
    n,m=a[0],-1
    for i in a[1:]:
        m,n=max(i-n,m),min(i,n)
    return m

print(max_profit([6, 5, 6, 95, 57, 73, 25, 28, 54, 38, 66, 17, 44, 3, 84, 68]))
print(max_profit([10, 9, 8, 7]))
print(max_profit([50, 38, 94, 5, 34]))