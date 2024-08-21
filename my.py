from statistics import mean

def array_center(a):
    b,c=mean(a),min(a)
    return [i for i in a if abs(i-b)<c]

print(array_center([8, 3, 4, 5, 2, 8]))
print(array_center([1, 3, 2, 1]))