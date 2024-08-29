from scipy.stats.mstats import gmean

def geometric_meanII(arr):
    if 0 in arr: return 0
    L = list(filter(lambda x: isinstance(x, int) and x > 0, arr))
    if 9 * len(arr) > 9 * len(L) + (len(L) if len(arr) > 10 else 9): return 0
    return gmean(L)

print(geometric_meanII([2, 2, 3, 2, 3, 2, 3, 4, 4])) 