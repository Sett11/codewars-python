def miss_nums_finder(a):
    m,u=max(a),set(a)
    return list(set(range(1,m+1))^u)

print(miss_nums_finder([8, 10, 11, 7, 3, 15, 6, 1, 14, 5, 12]))