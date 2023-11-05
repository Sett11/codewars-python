from statistics import median,mean

def mean_vs_median(a):
    b,c=mean(a),median(a)
    return ['mean','median'][b<c] if b!=c else 'same'


print(mean_vs_median([1, 2, 37]))
print(mean_vs_median([1, 1, 1]))