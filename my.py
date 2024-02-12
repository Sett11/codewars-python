from math import ceil

def avg_diags(a):
    n=len(a)
    v,w=[j for j in [a[n-i-1][i] for i in range(n)][::2] if j<0],[j for j in [a[i][i] for i in range(n)][1::2] if j>=0]
    return [round(sum(w)/len(w)),abs(round(sum(v)/len(v))) if v else -1]

print(avg_diags([
    [ 1,   3, -4,   5, -2,  5,  1], 
    [  2,   0, -7,   6,  8,  8, 15],
    [  4,   4, -2, -10,  7, -1,  7],
    [ -1,   3,  1,   0, 11,  4, 21],
    [ -7,   6, -4,  10,  5,  7,  6],
    [ -5,   4,  3,  -5,  7,  8, 17],
    [-11,   3,  4,  -8,  6, 16,  4]]))