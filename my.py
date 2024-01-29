def modified_sum(a,n):
    return sum(map(lambda x:x**n,a))-sum(a)

print(modified_sum([1,2,3],3))