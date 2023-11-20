def sort_it(a):
    return sorted(a,key=lambda e: e if type(e)==int else e[0])

print(sort_it([[3], 7, [9], [5], 1, 6, [0]]))