def validate_sequence(a):
    return len(set([a[i]-a[i-1] for i in range(1,len(a))]))==1

print(validate_sequence([0,2,4,6,8]))