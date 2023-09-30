def split_by_value(k,a):
    return [i for i in a if i<k]+[i for i in a if i>=k]

print(split_by_value(5, [1, 3, 5, 7, 6, 4, 2]))
print(split_by_value(6, [6, 4, 10, 10, 6]))