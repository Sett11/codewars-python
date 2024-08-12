from itertools import zip_longest as z

def vector_affinity(a,b):
    return sum(i==j for i,j in z(a,b,fillvalue='Fack'))/max(len(a),len(b)) if a and b else 1 if not a and not b else 0

print(vector_affinity([1,2,3,4],[1,2,3,5]))
print(vector_affinity([1,2,3], [1,2,3,4,5]))