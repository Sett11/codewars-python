def house_numbers_sum(a):
    return sum(a[slice(0,a.index(0))])

print(house_numbers_sum([5, 1, 2, 3, 0, 1, 5, 0, 2]))