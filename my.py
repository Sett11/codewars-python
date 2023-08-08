def sort_ranks(r):
    return [j if '&' not in j else j[3:] for j in sorted([i if i not in ['10','11'] else '99&'+i for i in r])]

k=['1', '10', '11', '2', '3', '4', '5', '6', '7', '8', '8.1', '8.1.1', '9']
print(sort_ranks(k))