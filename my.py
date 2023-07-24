def two_are_positive(a,b,c):
    return len([i for i in [a,b,c] if i>0])==2

print(two_are_positive(2,4,-6))