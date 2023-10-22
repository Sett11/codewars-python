def divisible_by_last(n):
    a=list(map(int,str(n)))
    return [False]+[not bool(a[i]%a[i-1]) if a[i-1] else False for i in range(1,len(a))]

print(divisible_by_last(73312))
print(divisible_by_last(2026))
print(divisible_by_last(635))