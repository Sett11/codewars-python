def is_information_consistent(a):
    return not bool(list(filter(lambda x:1 in x and -1 in x,zip(*a))))

print(is_information_consistent([
        [1,-1,0,1], 
        [1,-1,0,-1]]))