def sort_by_bit(a): 
    r=['0']*32
    for i in a:
        r[i]='1'
    return int(''.join(r[::-1]),2)

print(sort_by_bit([30, 0]))
print(sort_by_bit([1, 2, 0, 4]))