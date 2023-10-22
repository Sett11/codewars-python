def sort_by_binary_ones(a): 
    return sorted(a,key=lambda e:(-bin(e).count('1'),len(bin(e)),e))


print(sort_by_binary_ones([1,5,21,7,44,99,50,51,49,80,33,25]))