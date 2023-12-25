array_diff=lambda a,b:[i for i in a if i not in set(b)]

print(array_diff([-9, 16], [1, 0, -9, 9, -16, 4, -3, -12, -12, 8, 19, -10, 4, -1, -6]))