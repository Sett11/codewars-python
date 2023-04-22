def sort_by_value_and_index(a):
    r=[[(1+i)*j,j,i] for i,j in enumerate(a)]
    r.sort(key=lambda e:e[0] or e[2])
    return list(map(lambda e:e[1],r))

print(sort_by_value_and_index( [21, 55, 40, 53, 46, 67, 74, 56, 64, 2, 99, 76, 4, 3, 91, 95, 68, 41, 31, 100, 26, 14, 23, 67, 23, 5, 27, 83, 14, 93, 36, 67, 63, 73, 73, 84, 60, 90, 97, 50, 55, 58, 89, 51, 45, 87, 99, 38, 55, 83, 57, 41, 61, 71, 4, 88, 30, 83, 65, 33, 64, 84, 86]))