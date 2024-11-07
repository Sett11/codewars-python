def euclidean_distance(a,b):
    return round(sum((j-i)**2 for i,j in zip(a,b))**.5,2)