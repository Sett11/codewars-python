def even_numbers_before_fixed(a,n):
    return -1 if n not in a else len(list(filter(lambda e:e%2==0,a[slice(0,a.index(n))])))

print(even_numbers_before_fixed([1, 4, 2, 6, 3, 1], 6))