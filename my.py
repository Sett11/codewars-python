def is_orthogonal(a,b): 
    return not sum(a[i]*b[i] for i in range(len(a)))

print(is_orthogonal([-13,-26], [-8,4]))